
from sampleserve.core import db, BaseModel


class Test(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    active = db.Column(db.Boolean, default=True)
    sort = db.Column(db.Integer, default=0)
    title = db.Column(db.String(255), default='')
    abbrev = db.Column(db.String(128))
    preservative = db.Column(db.String(255))
    filter = db.Column(db.String(255))
    field = db.Column(db.Boolean, default=False)
    substance_ids = db.Column(db.Text)
    test_material_ids = db.Column(db.Text)
    test_material_qty = db.Column(db.Text)

    def __repr__(self):
        return '<Test {} ({})>'.format(self.title, self.id)


class TestMaterial(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), default='')
    active = db.Column(db.Boolean, default=True)
    sort = db.Column(db.Integer, default=0)
    bottle = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<TestMaterial {} ({})>'.format(self.title, self.id)


tests_substances = db.Table(
    'tests_substances',
    db.Column('test_id', db.Integer, db.ForeignKey('test.id'), default=0),
    db.Column('substance_id', db.Integer, db.ForeignKey('substance.id'), default=0),
)
