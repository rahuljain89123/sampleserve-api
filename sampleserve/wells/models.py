
from sampleserve.core import db, BaseModel


class Well(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    frequency_id = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(255), default='', index=True)
    top_of_casing = db.Column(db.Float(10), default=0.0)
    xpos = db.Column(db.Integer, default=0)
    ypos = db.Column(db.Integer, default=0)
    xpos_fields = db.Column(db.Integer, default=0)
    ypos_fields = db.Column(db.Integer, default=0)
    sort = db.Column(db.Integer, default=0)
    sampletechnique = db.Column(db.String(255), default='')
    material = db.Column(db.String(255))
    diameter = db.Column(db.Float(9))
    screenlength = db.Column(db.Float(9))
    est_depth_to_water = db.Column(db.Float(10))
    depth_to_bottom = db.Column(db.Float(9))
    purge_water_disposal = db.Column(db.String(255))
    latitude = db.Column(db.Float(9))
    longitude = db.Column(db.Float(9))
    notes = db.Column(db.Text)

    def __repr__(self):
        return '<Well {} ({})>'.format(self.title, self.id)


class WellImage(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'))
    sort = db.Column(db.Integer)
    last_modified = db.Column(db.Integer)
    height_md = db.Column(db.Integer)
    width_md = db.Column(db.Integer)
    width_sm = db.Column(db.Integer)
    height_sm = db.Column(db.Integer)
    url_md = db.Column(db.String(255))
    url_lg = db.Column(db.String(255))
    filestack_handle = db.Column(db.String(255))
    well = db.relationship('Well', backref=db.backref('well_image', lazy='dynamic', cascade='all'))

    def __repr__(self):
        return '<WellImage {}>'.format(self.id)


class Frequency(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    sort = db.Column(db.Integer)
    title = db.Column(db.String(255))
    timediff = db.Column(db.String(64))
    peryear = db.Column(db.Integer)
    unit = db.Column(db.String(64))
    default = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Frequency {} ({})>'.format(self.title, self.frequency_id)


well_date = db.Table(
    'well_date',
    db.Column('well_id', db.Integer, db.ForeignKey('well.id'), default=0),
    db.Column('active', db.Boolean, default=True),
    db.Column('position', db.Integer),
    db.Column('gaugeonly', db.Boolean, default=False),
    db.Column('test_ids', db.String(255)),
)

well_date_set = db.Table(
    'well_date_set',
    db.Column('site_id', db.Integer, db.ForeignKey('site.id')),
    db.Column('position', db.Integer),
    db.Column('date', db.Date),
    db.Column('schedule_id', db.Integer, default=None),
)

well_options = db.Table(
    'well_options',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('field', db.String(64)),
    db.Column('title', db.String(255)),
    db.Column('sort', db.Integer, default=0),
)
