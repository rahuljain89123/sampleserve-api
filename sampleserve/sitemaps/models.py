
from sampleserve.core import db, BaseModel


class SiteMap(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    title = db.Column(db.String(255))
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    url = db.Column(db.String(255))
    scale = db.Column(db.Float(12), default=1.0)
    site = db.relationship('Site', backref=db.backref('sitemaps', lazy='dynamic', cascade='all'))

    def __repr__(self):
        return '<SiteMap {} ({})>'.format(self.title, self.id)

    def json(self):
        res = dict()

        for field in self._fields():
            res[field] = getattr(self, field)

        res['wells'] = []

        for well in self.wells:
            res['wells'].append(well.json())

        return res


class SiteMapWell(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    site_map_id = db.Column(db.Integer, db.ForeignKey('site_map.id'))
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'))
    xpos = db.Column(db.Integer)
    ypos = db.Column(db.Integer)
    xpos_fields = db.Column(db.Integer)
    ypos_fields = db.Column(db.Integer)
    sitemap = db.relationship('SiteMap', backref=db.backref('wells', lazy='dynamic', cascade='all'))
    well = db.relationship('Well', lazy='joined')

    def __repr__(self):
        return '<SiteMapWell {} well:{} x:{} y:{}>'.format(self.id, self.well.title, self.xpos, self.ypos)
