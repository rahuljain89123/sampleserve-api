
# Views get initiated in frontend/__init__.property
from pprint import pprint
from datetime import date, timedelta, datetime

from flask import make_response, request, current_app, flash, redirect, \
    url_for, render_template, abort, g

from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import BooleanEqualFilter
from wtforms import PasswordField

from flask_bcrypt import Bcrypt
from flask_login import (
    login_required,
    current_user,
)

from sampleserve.core import db
from sampleserve.models import (
    Sample,
    SampleValue,
    SiteMap,
    SiteMapWell,
    Client,
    Upload,
    Site,
    SiteData,
    Contact,
    ScheduleWellTests,
    Schedule,
    SubstanceGroup,
    Substance,
    Criteria,
    State,
    Test,
    TestMaterial,
    User,
    Role,
    Transaction,
    UserDeprecated,
    RoleDeprecated,
    Consultant,
    Manager,
    Company,
    Sampler,
    Office,
    Lab,
    Well,
    WellImage,
    Frequency,
)
from sampleserve.users.auth import (
    auth_manager,
    bcrypt,
)
from sampleserve.reports.helpers import slugify
from sampleserve.util import id_generator
from sampleserve.emails.emails import (
    invite_user,
)
from .forms import OnboardLabForm


class AdminModel(ModelView):
    def is_accessible(self):
        return True


class LabView(AdminModel):
    can_create = True
    column_list = ('title', 'city', 'state', 'url',)
    column_searchable_list = ('title',)

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(LabView, self).__init__(Lab, session, **kwargs)


class UserView(AdminModel):
    can_create = True
    column_list = ('name', 'email',)
    column_searchable_list = ('name', 'email',)
    form_excluded_columns = ('password',)
    form_extra_fields = {
        'set_password': PasswordField('Set New Password')
    }

    def on_model_change(self, form, model, is_created):
        if form.email.data:
            # Strip spaces from the email
            form.email = form.email.data.strip()
        if form.set_password.data:
            model.password = bcrypt.generate_password_hash(form.set_password.data.strip())
            if is_created:
                model.active = True
                model.pending = False

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(UserView, self).__init__(User, session, **kwargs)


class SiteView(AdminModel):
    can_create = True

    column_list = ('lab.title', 'client.name', 'title', 'state',)
    column_searchable_list = ('lab.title', 'client.name', 'title', 'state',)

    def __init__(self, session, **kwargs):
        super(SiteView, self).__init__(Site, session, **kwargs)


class SampleView(AdminModel):
    # Disable model creation
    can_create = True

    # Override displayed fields
    column_list = ('date_collected', 'site.title',)
    column_filters = ('site_id',)

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(SampleView, self).__init__(Sample, session, **kwargs)


class SampleValueView(AdminModel):
    # Disable model creation
    can_create = True

    # Override displayed fields
    column_list = ('well.title', 'substance.title', 'sample.date_collected', 'value',)
    column_filters = ('substance_id', 'sample_id', 'well_id', 'well.title', 'free_product', 'sample.site_id', 'well.title', 'substance.title', 'sample.date_collected')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(SampleValueView, self).__init__(SampleValue, session, **kwargs)


class SubstanceView(AdminModel):
    # Disable model creation
    can_create = True

    # Override displayed fields
    column_list = ('title', 'cas', 'active', 'field_data',)
    column_searchable_list = ('title', 'cas', 'cas_sanitized',)
    column_filters = ('title', 'cas', 'active', 'field_data',)
    form_excluded_columns = ['cas_sanitized',]

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(SubstanceView, self).__init__(Substance, session, **kwargs)


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        users = User.query.filter_by().all()
        return self.render(
            'admin/index.html',
            users=users)


class OnboardLabView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        lab = None
        user = None
        form = OnboardLabForm()
        if form.validate_on_submit():
            print("Validated")
            # Create new lab
            lab = Lab(title=form.lab_name.data, url=slugify(form.lab_name.data))
            db.session.add(lab)
            db.session.commit()
            # Create LabAdmin and send invite
            user = User(
                email=form.email.data,
                name=form.name.data,
                role_id=2,
                active=False,
                pending=True,
                invite_code=id_generator(),
                lab_id=lab.id,
            )
            db.session.add(user)
            db.session.commit()
            # Send invitation to the User.
            invite_user(user=user)
            print("lab id: %d" % lab.id)
            flash("Sucessfully created lab and sent invitation!", "success")
            return redirect("/admin/onboardlabview/?lab_id=%d" % lab.id)
        if 'lab_id' in request.args:
            lab = Lab.query.get(request.args['lab_id'])
            user = User.query.filter_by(lab_id=lab.id, role_id=2).first()
        return self.render(
            'admin/onboard-lab.html',
            form=form,
            lab=lab,
            user=user)












