
from flask import g
from flask_login import current_user

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm.session import object_session
from sqlalchemy import event

from sampleserve.core import db, BaseModel
from sampleserve.users.models import User, Company


class Client(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.now())
    company = db.relationship('Company', backref=db.backref('clients', lazy='dynamic', cascade='all'))

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query
        elif g.current_role == 'LabAdmin' or g.current_role == 'LabAssociate':
            return self.query \
                .join(self.company) \
                .filter(Company.lab == g.current_lab)
        elif g.current_role == 'CompanyAdmin' or g.current_role == 'CompanyAssociate':
            return self.query \
                .join(self.company) \
                .join(Company.users) \
                .filter(Company.lab == g.current_lab) \
                .filter(User.id == current_user.id)
        elif g.current_role == 'ClientManager':
            return self.query \
                .join(self.company) \
                .join(self.users) \
                .filter(Company.lab == g.current_lab) \
                .filter(User.id == current_user.id)
        elif g.current_role == 'Technician':
            return self.query \
                .join(self.company) \
                .join(self.sites) \
                .join(Site.users) \
                .filter(Company.lab == g.current_lab) \
                .filter(User.id == current_user.id)

        return self.query.filter(False)

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['user_ids'] = []

        for user in self.users:
            res['user_ids'].append(user.id)

        return res

    def __repr__(self):
        return '<Client {} ({})>'.format(self.name, self.id)


class Upload(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    lab_id = db.Column(db.Integer, db.ForeignKey('lab.id'))
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
    upload_type = db.Column(db.String(255))
    sample_date = db.Column(db.DateTime)
    filename = db.Column(db.String(255))
    url = db.Column(db.String(255))
    sent = db.Column(db.Boolean, default=False)
    lab_upload = db.Column(db.Boolean, default=False)  # True if the lab uploaded this file rather than user
    lab = db.relationship('Lab', backref=db.backref('uploads', lazy='dynamic', cascade='all'))
    company = db.relationship('Company', backref=db.backref('uploads', lazy='dynamic', cascade='all'))

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query
        elif g.current_role == 'LabAdmin' or g.current_role == 'LabAssociate':
            return self.query \
                .join(self.company) \
                .filter(Company.lab == g.current_lab) \
                .order_by(Upload.created_at.desc())
        elif g.current_role == 'CompanyAdmin' or g.current_role == 'CompanyAssociate':
            return self.query \
                .join(self.company) \
                .join(Company.users) \
                .filter(Company.lab == g.current_lab) \
                .filter(User.id == current_user.id) \
                .order_by(Upload.created_at.desc())
        elif g.current_role == 'ClientManager':
            return self.query \
                .join(self.company) \
                .join(self.users) \
                .filter(Company.lab == g.current_lab) \
                .filter(User.id == current_user.id) \
                .order_by(Upload.created_at.desc())
        elif g.current_role == 'Technician':
            return self.query \
                .join(self.company) \
                .join(self.sites) \
                .join(Site.users) \
                .filter(Company.lab == g.current_lab) \
                .filter(User.id == current_user.id) \
                .order_by(Upload.created_at.desc())

    def __repr__(self):
        return '<Upload {} ({})>'.format(self.filename, self.id)

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['created_at'] = self.created_at.isoformat() + 'Z'

        return res


substances_sites = db.Table(
    'substances_sites',
    db.Column('substance_id', db.Integer, db.ForeignKey('substance.id')),
    db.Column('site_id', db.Integer, db.ForeignKey('site.id'), default=None),
    db.Column('sort', db.Integer, default=None),
)


class Site(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    additional_owner_ids = db.Column(JSON)
    consultant_id = db.Column(db.Integer)
    additional_consultant_ids = db.Column(JSON)
    sampler_id = db.Column(db.Integer)
    lab_id = db.Column(db.Integer, db.ForeignKey('lab.id'))
    manager_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.now())
    active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(255), index=True)
    sort = db.Column(db.Integer, default=0)
    facility_id = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    contact_phone = db.Column(db.String(255))
    contact_email = db.Column(db.String(255))
    notes = db.Column(db.Text)
    address = db.Column(db.String(255))
    city = db.Column(db.String(128))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(32))
    county = db.Column(db.String(64))
    latitude = db.Column(db.Float(9), default=0)
    longitude = db.Column(db.Float(9), default=0)
    start_sampling_on = db.Column(db.DateTime)
    history = db.Column(db.Text)
    background = db.Column(db.Text)
    summary = db.Column(db.Text)
    qaqc_duplicates = db.Column(db.Boolean, default=False)
    qaqc_duplicates_per_samples = db.Column(db.Integer, default=0)
    qaqc_duplicates_type = db.Column(db.String(16))
    qaqc_duplicates_well_ids = db.Column(JSON)
    qaqc_duplicates_test_ids = db.Column(JSON)
    qaqc_msmsds = db.Column(db.Boolean, default=False)
    qaqc_msmsds_per_samples = db.Column(db.Integer, default=0)
    qaqc_msmsds_type = db.Column(db.String(16))
    qaqc_msmsds_well_ids = db.Column(JSON)
    qaqc_msmsds_test_ids = db.Column(JSON)
    qaqc_fieldblanks = db.Column(db.Boolean, default=False)
    qaqc_fieldblanks_per_samples = db.Column(db.Integer, default=0)
    qaqc_fieldblanks_type = db.Column(db.String(16))
    qaqc_fieldblanks_test_ids = db.Column(JSON)
    qaqc_tripblanks = db.Column(db.Boolean, default=False)
    qaqc_tripblanks_per_samples = db.Column(db.Integer, default=0)
    qaqc_tripblanks_type = db.Column(db.String(16))
    qaqc_tripblanks_test_ids = db.Column(JSON)
    qaqc_equipmentblanks = db.Column(db.Boolean, default=False)
    qaqc_equipmentblanks_per_samples = db.Column(db.Integer, default=0)
    qaqc_equipmentblanks_type = db.Column(db.String(16))
    qaqc_equipmentblanks_test_ids = db.Column(JSON)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    lab = db.relationship('Lab', backref=db.backref('sites', lazy='dynamic', cascade='all'))
    client = db.relationship('Client', backref=db.backref('sites', lazy='dynamic', cascade='all'))
    wells = db.relationship('Well', backref='sites', lazy='dynamic', cascade='all')
    substances = db.relationship('Substance', secondary=substances_sites, lazy='dynamic', backref=db.backref('sites', lazy='dynamic'))
    data = db.relationship('SiteData', backref=db.backref('sites', lazy='joined', cascade='all'))

    def __repr__(self):
        return '<Site {} ({})>'.format(self.title, self.id)

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query.filter_by(lab_id=g.current_lab.id)
        elif g.current_role == 'LabAdmin' or g.current_role == 'LabAssociate':
            return self.query.filter_by(lab_id=g.current_lab.id)
        elif g.current_role == 'CompanyAdmin' or g.current_role == 'CompanyAssociate':
            return self.query \
                .join(self.client) \
                .join(Client.company) \
                .join(Company.users) \
                .filter(self.lab == g.current_lab) \
                .filter(User.id == current_user.id)
        elif g.current_role == 'ClientManager':
            return self.query \
                .join(self.client) \
                .join(Client.users) \
                .filter(self.lab == g.current_lab) \
                .filter(User.id == current_user.id)
        elif g.current_role == 'Technician':
            return self.query \
                .join(self.users) \
                .filter(self.lab == g.current_lab) \
                .filter(User.id == current_user.id)

        return self.query.filter(False)

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['user_ids'] = []

        for user in self.users:
            res['user_ids'].append(user.id)

        # Append wells
        res['well_ids'] = []

        for well in self.wells:
            res['well_ids'].append(well.id)

        # Append substances
        res['substance_ids'] = []

        for substance in self.substances:
            res['substance_ids'].append(substance.id)

        return res


@event.listens_for(Site, 'after_insert')
def receive_after_insert(mapper, connection, target):
    "listen for the 'after_insert' event"
    site_data_table = SiteData.__table__
    connection.execute(
        site_data_table.insert().
        values(site_id=target.id)
    )
    # site_data = SiteData(site_id=target.id)
    # db.session.add(site_data)
    # db.session.commit()


class SiteData(BaseModel):
    __tablename__ = 'site_data'
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    contact_qc = db.Column(db.Boolean(), default=False)
    date_release_discovered = db.Column(db.DateTime())
    confirmed_release_number = db.Column(db.Text())
    site_classification = db.Column(db.Integer())
    previous_classification = db.Column(db.Integer())

    # Type of RBCA Evaluation, Tier 1, Tier 2, or Tier 3
    type_of_rbca_evaluation = db.Column(db.String(255))

    # Substances released
    substances_released_gasoline = db.Column(db.Boolean())
    substances_released_diesel = db.Column(db.Boolean())
    substances_released_ethanol = db.Column(db.Boolean())
    substances_released_ethanol_e10 = db.Column(db.Boolean())
    substances_released_ethanol_e85 = db.Column(db.Boolean())
    substances_released_other = db.Column(db.String(255))

    # Has contamination migrated off-site above Tier 1 Residential RBSLs?
    contamination_migrated_off_site = db.Column(db.Boolean, default=False)
    impacted_parties_notified = db.Column(db.Boolean, default=False)

    # Predominant groundwater flow direction
    groundwater_flow_direction = db.Column(db.String(255))
    depth_to_groundwater = db.Column(db.String(255))

    # is mobile NAPL present?
    mobile_napl_present_currently = db.Column(db.Boolean, default=False)
    mobile_napl_present_previously = db.Column(db.Boolean, default=False)
    mobile_napl_present_recovered = db.Column(db.Boolean, default=False)
    mobile_napl_present_recovered_gallons = db.Column(db.String(255))
    mobile_napl_present_recovered_date = db.Column(db.String(255))

    # is migrating NAPL present?
    migrating_napl_present_currently = db.Column(db.Boolean, default=False)
    migrating_napl_actions_taken = db.Column(db.Boolean, default=False)

    # Since last report
    soil_remediated_since_last_report = db.Column(db.String(255))
    groundwater_remediated_since_last_report = db.Column(db.String(255))
    soil_remediated = db.Column(db.String(255))
    groundwater_remediated = db.Column(db.String(255))

    # Have toxic vapors?
    vapors_in_confined_space = db.Column(db.Boolean, default=False)

    # Drinking water supply affected?
    drinking_water_affected_currently = db.Column(db.Boolean, default=False)
    drinking_water_affected_previously = db.Column(db.Boolean, default=False)
    drinking_water_affected_private = db.Column(db.Boolean, default=False)
    drinking_water_affected_private_num_wells = db.Column(db.Integer())
    drinking_water_affected_public = db.Column(db.Boolean, default=False)
    drinking_water_affected_public_num_wells = db.Column(db.Integer())
    drinking_water_affected_municiple = db.Column(db.Boolean, default=False)
    drinking_water_affected_municiple_num_wells = db.Column(db.Integer())

    # Surface water been contaminated?
    surface_water_contaminated = db.Column(db.Boolean, default=False)

    # Estimated distance and direction from point of release to nearest
    point_of_release_to_private_well = db.Column(db.String(255))
    point_of_release_to_municipal_well = db.Column(db.String(255))
    point_of_release_to_surface_water = db.Column(db.String(255))

    # Is site within a wellhead protection zone?
    wellhead_protection_zone = db.Column(db.Boolean, default=False)

    # Type of report:
    report_type = db.Column(db.String(255))
    report_type_other = db.Column(db.String(255))

    def __repr__(self):
        return '<SiteData {}>'.format(self.id)


class Contact(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city = db.Column(db.String(128))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(32))
    contact = db.Column(db.String(255))
    phone = db.Column(db.String(32))
    cell = db.Column(db.String(32))
    fax = db.Column(db.String(32))
    email = db.Column(db.String(255))
    notes = db.Column(db.Text)
    type = db.Column(db.Text)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    site = db.relationship('Site', backref=db.backref('contacts', lazy='dynamic', cascade='all'))

    @hybrid_property
    def role_query(self):
        if g.current_role == 'Admin':
            return self.query
        elif g.current_role == 'LabAdmin' or g.current_role == 'LabAssociate':
            return self.query.filter_by(lab_id=g.current_lab.id)
        elif g.current_role == 'CompanyAdmin' or g.current_role == 'CompanyAssociate':
            return self.query \
                .join(self.site) \
                .join(Site.client) \
                .join(Client.company) \
                .join(Company.users) \
                .filter(self.lab == g.current_lab) \
                .filter(User.id == current_user.id)
        elif g.current_role == 'ClientManager':
            return self.query \
                .join(self.site) \
                .join(Site.client) \
                .join(Client.users) \
                .filter(self.lab == g.current_lab) \
                .filter(User.id == current_user.id)
        elif g.current_role == 'Technician':
            return self.query \
                .join(self.site) \
                .join(Site.users) \
                .filter(self.lab == g.current_lab) \
                .filter(User.id == current_user.id)

        return self.query.filter(False)

    def __repr__(self):
        return '<Contact {} ({})>'.format(self.title, self.id)


schedule_tests = db.Table(
    'schedule_tests',
    db.Column('schedule_id', db.Integer, db.ForeignKey('schedule.id')),
    db.Column('test_id', db.Integer, db.ForeignKey('test.id'), default=None),
)


class ScheduleWellTests(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'))
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))

    def __repr__(self):
        return '<ScheduleWellTests {}>'.format(self.id)


gauged_wells = db.Table(
    'gauged_wells',
    db.Column('schedule_id', db.Integer(), db.ForeignKey('schedule.id')),
    db.Column('well_id', db.Integer(), db.ForeignKey('well.id'))
)

skipped_wells = db.Table(
    'skipped_wells',
    db.Column('schedule_id', db.Integer(), db.ForeignKey('schedule.id')),
    db.Column('well_id', db.Integer(), db.ForeignKey('well.id'))
)


class Schedule(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    finished = db.Column(db.Boolean, default=False)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), default=0)
    date = db.Column(db.DateTime)
    timeofday = db.Column(db.String(255))
    starttime = db.Column(db.String(16))
    endtime = db.Column(db.String(16))
    typeofactivity = db.Column(db.String(255))
    release_number = db.Column(db.String(255))
    frequency_association = db.Column(db.String(255))
    test_ids = db.Column(JSON)
    tests = db.relationship('Test', secondary=schedule_tests,
                            backref=db.backref('schedules', lazy='dynamic', cascade='all'))
    site = db.relationship('Site', backref=db.backref('schedules', lazy='dynamic', cascade='all'))
    schedule_well_tests = db.relationship('ScheduleWellTests', lazy='dynamic', cascade='all')
    gauged_wells = db.relationship('Well', secondary=gauged_wells, lazy='dynamic', cascade='all')
    skipped_wells = db.relationship('Well', secondary=skipped_wells, lazy='dynamic', cascade='all')

    def __repr__(self):
        return '<Schedule {}>'.format(self.id)

    @hybrid_property
    def role_query(self):
        return self.query

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['test_ids'] = []

        for test in self.tests:
            res['test_ids'].append(test.id)

        res['gauged_well_ids'] = []

        for gauged_well in self.gauged_wells:
            res['gauged_well_ids'].append(gauged_well.id)

        res['skipped_well_ids'] = []

        for skipped_well in self.skipped_wells:
            res['skipped_well_ids'].append(skipped_well.id)

        return res
