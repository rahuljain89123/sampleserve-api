
from sqlalchemy.orm import validates

from sampleserve.core import db, BaseModel
from pprint import pprint


class SubstanceGroup(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default=True, index=True)
    hard_ref = db.Column(db.Integer, nullable=False, default=0)
    title = db.Column(db.String(255), nullable=False, default='', index=True)
    sort = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<SubstanceGroup {} ({})>'.format(self.title, self.id)


class Substance(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    substance_group_id = db.Column(db.Integer, db.ForeignKey('substance_group.id'), nullable=False, default=0)
    active = db.Column(db.Boolean, default=False, index=True)
    hard_ref = db.Column(db.Integer, default=0)
    title = db.Column(db.String(255), index=True)
    abbreviation = db.Column(db.String(255))
    cas = db.Column(db.String(255))
    cas_sanitized = db.Column(db.String(255), index=True)
    sort = db.Column(db.Integer, default=0)
    unit = db.Column(db.String(16))
    precision = db.Column(db.Integer, default=2)
    criteria = db.Column(db.Float(12), default=0.0)
    field_data = db.Column(db.Boolean, default=False)

    @validates('cas')
    def update_slug(self, key, cas):
        if cas and len(cas):
            self.cas_sanitized = cas.replace('-', '').replace(' ', '').upper()
            return cas

    def __repr__(self):
        return '<Substance {} ({})>'.format(self.title, self.id)


class Criteria(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(10), nullable=False)
    values = db.relationship('CriteriaValues', backref=db.backref('criteria', cascade='all'))

    def __repr__(self):
        return '<Criteria {} ({})>'.format(self.title, self.id)


class CriteriaValues(BaseModel):
    __tablename__ = "criteria_values"
    id = db.Column(db.Integer, primary_key=True)
    criteria_id = db.Column(db.Integer, db.ForeignKey('criteria.id'), nullable=False)
    substance_id = db.Column(db.Integer, db.ForeignKey('substance.id'), nullable=False)
    value = db.Column(db.Float(12), nullable=False)


class State(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    abbreviation = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return '<State {} ({})>'.format(self.title, self.id)


substance_state_names = db.Table(
    'substance_state_names',
    db.Column('substance_id', db.Integer, db.ForeignKey('substance.id'), nullable=False),
    db.Column('state_id', db.Integer, db.ForeignKey('state.id'), nullable=False),
    db.Column('title', db.String(255), nullable=False),
)
