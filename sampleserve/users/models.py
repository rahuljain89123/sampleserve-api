
import datetime
from flask import g
from flask_login import current_user, UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import JSON

from sampleserve.core import db, BaseModel
from sampleserve.helpers import firstname


users_companies = db.Table(
    'users_companies',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('company_id', db.Integer, db.ForeignKey('company.id')),
)

users_clients = db.Table(
    'users_clients',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('client_id', db.Integer, db.ForeignKey('client.id')),
)

users_sites = db.Table(
    'users_sites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('site_id', db.Integer, db.ForeignKey('site.id')),
)


class User(UserMixin, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    lab_id = db.Column(db.Integer, db.ForeignKey('lab.id'))
    invitee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    photo_url = db.Column(db.String(255))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=False)
    pending = db.Column(db.Boolean(), default=True)
    phone = db.Column(db.String(15))
    invite_code = db.Column(db.String(255))
    reset_code = db.Column(db.String(255))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))
    lab = db.relationship('Lab', backref=db.backref('users', lazy='dynamic'))
    invitee = db.relationship('User', uselist=False, remote_side=[id], backref=db.backref('invites', uselist=False))
    companies = db.relationship('Company', secondary=users_companies, lazy='dynamic', backref=db.backref('users', lazy='dynamic', cascade='all'))
    clients = db.relationship('Client', secondary=users_clients, lazy='dynamic', backref=db.backref('users', lazy='dynamic', cascade='all'))
    sites = db.relationship('Site', secondary=users_sites, lazy='dynamic', backref=db.backref('users', lazy='dynamic', cascade='all'))

    def __repr__(self):
        return '<User {} ({})>'.format(self.email, self.id)

    @property
    def public_fields(self):
        return ['id', 'email', 'name', 'photo_url', 'phone', 'active', 'role_id', 'lab_id', 'company_ids', 'client_ids', 'site_ids']

    @property
    def is_active(self):
        return self.active

    @property
    def company_ids(self):
        return [company.id for company in self.companies.all()]

    @property
    def client_ids(self):
        return [client.id for client in self.clients.all()]

    @property
    def site_ids(self):
        return [site.id for site in self.sites.all()]

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['company_ids'] = self.company_ids
        res['client_ids'] = self.client_ids
        res['site_ids'] = self.client_ids

        # Set first name
        res['firstname'] = firstname(self.name)
        return res

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query
        elif g.current_role == 'Anonymous':
            return self.query.filter_by(lab=g.current_lab, pending=True)

        return self.query.filter_by(lab=g.current_lab)


class Role(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Role {} ({})>'.format(self.name, self.id)

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query
        elif g.current_role == 'Anonymous':
            return self.query.filter(False)
        else:
            return self.query.filter(self.id >= current_user.role.id)


class Transaction(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lab_id = db.Column(db.Integer, db.ForeignKey('lab.id'))
    site_id = db.Column('site_id', db.Integer, db.ForeignKey('site.id'))
    company_id = db.Column('company_id', db.Integer, db.ForeignKey('company.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
    total_amount = db.Column(db.Float(12))
    lab_earnings_amount = db.Column(db.Float(12))
    samples = db.Column(JSON)
    stripe_transaction_id = db.Column(db.String(255))
    stripe_card_id = db.Column(db.String(255))
    cc_last4 = db.Column(db.Integer)
    user = db.relationship('User', backref=db.backref('transactions', lazy='dynamic'))

    def __repr__(self):
        return '<Transaction {} ({})>'.format(self.total_amount, self.id)


class UserDeprecated(BaseModel):
    user_id = db.Column(db.Integer, primary_key=True)
    user_role_id = db.Column(db.Integer, db.ForeignKey('role_deprecated.user_role_id'), default=0)
    username = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), default='')
    require_password_change = db.Column(db.Boolean, default=True)
    suspended = db.Column(db.Boolean, default=False)
    login_timestamp = db.Column(db.Integer, default=0)
    failed_login_timestamp = db.Column(db.Integer, default=0)
    login_failures = db.Column(db.Integer, default=0)
    hash_timestamp = db.Column(db.Integer, default=0)
    access = db.Column(db.Text)
    info = db.Column(db.Text)
    name = db.Column(db.String(255), default=None)
    company = db.Column(db.String(255), default=None)
    address = db.Column(db.String(255), default=None)
    phone = db.Column(db.String(255), default=None)
    fax = db.Column(db.String(255), default=None)
    created = db.Column(db.DateTime, default=db.func.now())
    id = db.Column(db.Integer)

    def __repr__(self):
        return '<UserDeprecated {} ({})>'.format(self.username, self.user_id)


class RoleDeprecated(BaseModel):
    user_role_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), default='')
    access = db.Column(db.Text)

    def __repr__(self):
        return '<RoleDeprecated {} ({})>'.format(self.title, self.user_role_id)


class Consultant(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    qcid = db.Column(db.String(32))
    title = db.Column(db.String(255), default='')
    address = db.Column(db.String(255))
    city = db.Column(db.String(128))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(32))
    contact = db.Column(db.String(255), default='')
    phone = db.Column(db.String(32))
    cell = db.Column(db.String(32))
    fax = db.Column(db.String(32))
    email = db.Column(db.String(255))
    notes = db.Column(db.Text)

    def __repr__(self):
        return '<Consultant {} ({})>'.format(self.title, self.id)


class Manager(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(255), default='')
    address = db.Column(db.String(255))
    city = db.Column(db.String(128))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(32))
    contact = db.Column(db.String(255), default='')
    phone = db.Column(db.String(32))
    cell = db.Column(db.String(32))
    fax = db.Column(db.String(32))
    email = db.Column(db.String(255))
    notes = db.Column(db.Text)

    def __repr__(self):
        return '<Manager {} ({})>'.format(self.title, self.id)


class Company(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), default='')
    active = db.Column(db.Boolean, default=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(128))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(32))
    contact = db.Column(db.String(255), default='')
    phone = db.Column(db.String(32))
    cell = db.Column(db.String(32))
    fax = db.Column(db.String(32))
    email = db.Column(db.String(255))
    notes = db.Column(db.Text)
    lab_id = db.Column(db.Integer, db.ForeignKey('lab.id'))
    lab = db.relationship('Lab', backref=db.backref('companies', lazy='dynamic', cascade='all'))
    sites = db.relationship('Site', lazy='dynamic', backref='companies', cascade='all')

    def __repr__(self):
        return '<Company {} ({})>'.format(self.title, self.id)

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query.filter_by(lab_id=g.current_lab.id)
        elif g.current_role == 'LabAdmin' or g.current_role == 'LabAssociate':
            return self.query.filter_by(lab_id=g.current_lab.id)
        elif g.current_role == 'CompanyAdmin' or g.current_role == 'CompanyAssociate':
            return current_user.companies.filter_by(lab_id=g.current_lab.id)
        elif g.current_role == 'ClientManager' or g.current_role == 'Technician':
            return current_user.companies

        return self.query.filter_by(lab_id=g.current_lab.id)

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['user_ids'] = []

        for user in self.users:
            res['user_ids'].append(user.id)

        # Set is_deletable to True if the company has no active users
        res['is_deletable'] = not bool(self.users.filter_by(active=True).count())

        return res


class Sampler(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city = db.Column(db.String(128))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(32))
    contact = db.Column(db.String(255), default='')
    phone = db.Column(db.String(32))
    cell = db.Column(db.String(32))
    fax = db.Column(db.String(32))
    email = db.Column(db.String(255))
    notes = db.Column(db.Text)

    def __repr__(self):
        return '<Sampler {} ({})>'.format(self.title, self.id)


class Office(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    contact = db.Column(db.String(255), default=None)
    address = db.Column(db.String(80))
    city = db.Column(db.String(255))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(32))
    phone = db.Column(db.String(32), default=None)
    cell = db.Column(db.String(32), default=None)
    email = db.Column(db.String(255), default=None)
    lat = db.Column(db.Float(10))
    lng = db.Column(db.Float(10))

    def __repr__(self):
        return '<Office {} ({})>'.format(self.title, self.id)


class Lab(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(255), default='')
    address = db.Column(db.String(255), default='')
    city = db.Column(db.String(128), default='')
    state = db.Column(db.String(64), default='')
    zip = db.Column(db.String(32), default='')
    phone = db.Column(db.String(255), default='')
    contact = db.Column(db.String(255), default='')
    cell = db.Column(db.String(32))
    fax = db.Column(db.String(32))
    email = db.Column(db.String(255))
    notes = db.Column(db.Text)
    shipping_company = db.Column(db.String(255), default='')
    shipping_account = db.Column(db.String(255), default='')
    shipping_notes = db.Column(db.Text)
    url = db.Column(db.Text, unique=True)
    photo_url = db.Column(db.String(255))

    def __repr__(self):
        return '<Lab {} ({})>'.format(self.title, self.id)

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query

        return self.query.filter_by(id=g.current_lab.id)

