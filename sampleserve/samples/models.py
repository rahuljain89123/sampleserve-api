
import datetime

from sampleserve.core import db, BaseModel


class Sample(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'), unique=True, default=None)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), default=0)
    upload_id = db.Column(db.Integer, db.ForeignKey('upload.id'), default=None)
    active = db.Column(db.Boolean, default=True)
    date_collected = db.Column(db.Date)
    date_extracted = db.Column(db.Date)
    date_analyzed = db.Column(db.Date)
    site = db.relationship('Site', backref=db.backref('samples', lazy='dynamic', cascade='all'))
    schedule = db.relationship('Schedule', backref=db.backref('samples', lazy='dynamic', cascade='all'))

    def __repr__(self):
        return '<Sample {}>'.format(self.id)

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['qty_values'] = self.values.count()
        res['substance_ids'] = []

        # Convert the dates to the format we want
        if self.date_collected:
            res['date_collected'] = self.date_collected.strftime("%Y-%m-%d")
        if self.date_extracted:
            res['date_extracted'] = self.date_extracted.strftime("%Y-%m-%d")
        if self.date_analyzed:
            res['date_analyzed'] = self.date_analyzed.strftime("%Y-%m-%d")

        for value in self.values:
            if value.substance.id not in res['substance_ids']:
                res['substance_ids'].append(value.substance.id)

        return res


class SampleValue(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    substance_id = db.Column(db.Integer, db.ForeignKey('substance.id'), default=0)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'), default=0)
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'), default=0)
    upload_id = db.Column(db.Integer, db.ForeignKey('upload.id'), default=None)
    value = db.Column(db.Float(12), default=0.0)
    free_product = db.Column(db.Boolean, default=False)
    non_detect = db.Column(db.Boolean, default=False)
    less_than = db.Column(db.Float(12), default=0.0)  # Save less than values for the sticklers
    details = db.Column(db.String(20), default=None)
    new = db.Column(db.Boolean, default=True)
    paid_level_1 = db.Column(db.Boolean, default=False)
    paid_level_2 = db.Column(db.Boolean, default=False)
    sample = db.relationship('Sample', backref=db.backref('values', lazy='dynamic', cascade='all'))
    substance = db.relationship('Substance', lazy='joined')
    well = db.relationship('Well', backref=db.backref('sample_values', lazy='dynamic', cascade='all'))

    def __repr__(self):
        return '<SampleValue {}>'.format(self.id)
