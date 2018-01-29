import httplib

from pprint import pprint
from flask import abort, g, jsonify, Blueprint
from flask_login import current_user

from sampleserve.rest.views import BaseView
from sampleserve.rest.errors import (
    IntegrityError,
    handle_unauthorized,
    UnprocessableEntity,
    BadInvite,
    FormError,
)
from sampleserve.rest.validators import validate_schema

from . import schemas
from .auth import bcrypt
from .models import (
    User,
    Role,
    Company,
    Consultant,
    Manager,
    Sampler,
    Office,
    Lab
)
from .forms import InquiryForm
from sampleserve.sites.models import Client
from sampleserve.emails.emails import (
    invite_user,
    accepted_invite,
    free_trial_inquiry,
)
from sampleserve.util import id_generator


class UsersView(BaseView):
    model = User

    def post(self):
        if g.current_role in schemas.user:
            validate_schema(g.body, schemas.user[g.current_role])

        if 'email' not in g.body or not g.body['email'].strip():
            print("The issue is here")
            raise UnprocessableEntity('Invalid email')

        existing_user = self.model.query.filter_by(lab=g.current_lab, email=g.body['email']).first()
        if existing_user:
            # User already exists, add the permissions to their existing account
            # User cannot change roles, they cannot be a CompanyAdmin on one company but a CompanyAssociate on another.
            # They cannot be a CompanyAdmin and a ClientManager
            # The cannot be on multiple companies
            # This is because the role_id is set on the user object, and the role is used to determine whether to show LabApp, CompanyApp, ClientApp, or Siteapp.
            # A ClientManager can have many clients, a Technician can have many sites

            # Make sure the role_id matches the user's current role
            if 'role_id' in g.body and existing_user.role.id != g.body['role_id']:
                raise BadInvite('User role cannot be changed from %s' % existing_user.role.name)

            # User cannot currently belong to more than one company, so let's just give the invitee a nice error message
            if 'companies' in g.body:
                for company_id in g.body['companies']['add']:
                    if company_id in existing_user.company_ids:
                        raise BadInvite('Email already exists with this company.')
                    else:
                        raise BadInvite('Email is already associated with another company.')

            # Add clients to a ClientManager
            if 'clients' in g.body:
                for client_id in g.body['clients']['add']:
                    if existing_user.clients.filter_by(id=client_id).count():
                        raise BadInvite('Email is already associated with this client.')
                    else:
                        existing_user.patch(g.body)
                        existing_user.save_or_error()
                        res = existing_user.json()
                        return jsonify(res)

            # Add sites to a Technician
            if 'sites' in g.body:
                for site_id in g.body['sites']['add']:
                    if existing_user.sites.filter_by(id=site_id).count():
                        raise BadInvite('Email is already associated with this site.')
                    else:
                        existing_user.patch(g.body)
                        existing_user.save_or_error()
                        res = existing_user.json()
                        return jsonify(res)

            # Catchall Integrity Error
            raise IntegrityError('email')

        user = self.model()
        user.patch(g.body)

        # Check if sampleserve admin, override the role.
        if current_user.role_id != 1:
            user.lab = g.current_lab

        if 'password' in g.body:
            user.password = bcrypt.generate_password_hash(g.body['password'])
            user.pending = False
            user.active = True  # switch to false once email confirmation is working
            user.save_or_error()
            res = user.json()
            return jsonify(res)

        if current_user.is_anonymous:
            abort(httplib.UNAUTHORIZED)

        user.invitee = current_user
        user.pending = True
        user.active = False
        user.invite_code = id_generator()
        user.save_or_error()

        # Send email invite to the user
        invite_user(user=user)

        res = user.json()
        return jsonify(res)

    def patch(self, id):
        if g.current_role not in ['Admin', 'Anonymous'] and current_user.id == id:
            g.current_role = 'Own'

        print("g.current_role", g.current_role)
        if g.current_role in schemas.user:
            validate_schema(g.body, schemas.user[g.current_role])

        user = self.model.role_query.filter_by(id=id).first_or_404()

        if 'email' in g.body and g.body['email'] != user.email:
            if self.model.query.filter_by(lab=g.current_lab, email=g.body['email']).first():
                # Raise error if email already exist
                raise IntegrityError('email', message="Email already exists for this lab")
            if not user.active and current_user.id != user.id:
                # User is not active and email is changing, lets send them a new invite
                # Make sure current_user is authorized:
                if g.current_role not in ['Admin', 'LabAdmin', 'LabAssociate']:
                    abort(httplib.UNAUTHORIZED)
                user.invitee = current_user
                invite_user(user=user)

        # If the user is a company admin, create the first client.
        if user.role_id == 4:
            company = user.companies.first()
            # Check to see if there are any clients
            if not Client.query.filter_by(company_id=company.id).count():
                client = Client(company_id=company.id, name="My Client")
                client.save_or_error()

        user.patch(g.body)

        if 'password' in g.body:
            user.password = bcrypt.generate_password_hash(g.body['password'])
            user.pending = False
            user.active = True
            # Trigger accepted invitiation email
            accepted_invite(user=user)

        if 'active' in g.body and g.body['active']:
            # User is getting patched to Active, lets make sure the password is set
            if not user.password:
                abort(httplib.UNAUTHORIZED)

        user.save_or_error()
        res = user.json()
        return jsonify(res)


class ConsultantsView(BaseView):
    model = Consultant


class ManagersView(BaseView):
    model = Manager


class SamplersView(BaseView):
    model = Sampler


class OfficesView(BaseView):
    model = Office


class LabsView(BaseView):
    model = Lab


class RolesView(BaseView):
    model = Role


class CompaniesView(BaseView):
    model = Company

    def post(self):
        # Validate the company
        if g.current_role in schemas.company:
            validate_schema(g.body, schemas.company[g.current_role])

        if self.model.query.filter_by(lab_id=g.current_lab.id, title=g.body['title']).first():
            raise IntegrityError('title', message="This company already exists.")

        company = self.model()
        company.patch(g.body)

        # Check to see if a primary_user object has been passed
        if 'primary_user' in g.body:
            # Validate the user
            if g.current_role in schemas.user:
                validate_schema(g.body['primary_user'], schemas.user[g.current_role])
            # Check for existing user email
            if User.query.filter_by(lab=g.current_lab, email=g.body['primary_user']['email']).first():
                raise IntegrityError('email')

            # Everything has passed, save the user and the company together
            user = User()
            user.patch(g.body['primary_user'])
            user.invitee = current_user
            user.invite_code = id_generator()
            company.users.append(user)
            # Send the user invitation
            invite_user(user=user)

        company.save_or_error()
        res = company.json()
        return jsonify(res)


bplabs = Blueprint('labs', __name__, url_prefix='/labs', template_folder='templates')


@bplabs.route('/')
def listall():
    labs = Lab.query.filter(Lab.title.isnot(None)).all()
    res = [lab.json() for lab in labs if lab.title]
    return jsonify(res)


@bplabs.route('/start-free-trial', methods=["POST"])
def start_free_trial():
    form = InquiryForm()
    if form.validate_on_submit():
        free_trial_inquiry(
            name=form.name.data,
            company_name=form.company_name.data,
            email=form.email.data,
            phone=form.phone.data,
            number_of_employees=form.number_of_employees.data if form.number_of_employees.data != "Select Number of Employees" else None,
        )
        return jsonify(ok=True)
    raise FormError(errors=form.errors)


users = UsersView.as_view('users')
consultants = ConsultantsView.as_view('consultants')
companies = CompaniesView.as_view('companies')
managers = ManagersView.as_view('managers')
samplers = SamplersView.as_view('samplers')
offices = OfficesView.as_view('offices')
labs = LabsView.as_view('labs')
roles = RolesView.as_view('roles')
