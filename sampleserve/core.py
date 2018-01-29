
"""

Extends the Flask-SQLAlchemy default Model in a couple ways:

    fields() - List fields for updating object properties in one call.
    patch() - Assigns every JSON value in an object to the model.
    json() - Returns a JSON representation of the model.
    public_fields - Limits the fields that are returned in JSON.

Mostly for Postgres constraint violations (like unique constraint or foreign key):

    save_or_error() - Catches database errors and returns nice responses on save.
    delete_or_error() - Catches database errors and returns nice responses on delete.

"""

import re

from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy

from sampleserve.rest.errors import UnprocessableEntity

db = SQLAlchemy()

UNIQUE_CONTRAINT_RE = r"\(psycopg2\.IntegrityError\) duplicate key value violates unique constraint.*\n.*Key \((.*?)\)"
REMOVE_ABSENT_VALUE_RE = r"ValueError: list.remove(x): x not in list"


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def _fields(cls):
        return [prop.key for prop in db.class_mapper(cls).iterate_properties
                if isinstance(prop, db.ColumnProperty)]

    @classmethod
    def _relations(cls):
        relationships = cls.__mapper__.relationships
        classes = [r.mapper.class_ for r in relationships]
        names = relationships.keys()

        return dict(zip(names, classes))

    def __init__(self, *args, **kwargs):
        if args:
            for field, value in zip(self._fields(), args):
                setattr(self, field, value)
        elif kwargs:
            for field in kwargs:
                setattr(self, field, kwargs[field])

    def json(self):
        res = dict()

        for field in self._fields():
            if not hasattr(self, 'public_fields') or field in self.public_fields:
                res[field] = getattr(self, field)
        return res

    def patch(self, object):
        fields = self._fields()
        relations = self._relations()

        for key, value in object.items():
            if key in fields:
                setattr(self, key, value)
            elif key in relations:
                if isinstance(value, dict) and 'add' in value and 'remove' in value:
                    for id in value['add']:
                        if relations[key].query.get(id) not in getattr(self, key):
                            rel = relations[key].query.get(id)
                            if rel:
                                getattr(self, key).append(rel)
                    for id in value['remove']:
                        if relations[key].query.get(id) in getattr(self, key):
                            rel = relations[key].query.get(id)
                            if rel:
                                getattr(self, key).remove(rel)

    def save_or_error(self):
        db.session.add(self)

        try:
            db.session.commit()
        except IntegrityError as error:
            msg = 'Saving failed.'
            errors = []
            print(error.message)

            unique = re.match(UNIQUE_CONTRAINT_RE, error.message)

            if unique:
                key = unique.group(1)
                msg = 'Value of key \'{}\' must be unique.'.format(key)
                errors.append(dict(
                    key=key,
                    validator='unique_constraint',
                ))
            else:
                errors = [msg]

            raise UnprocessableEntity(msg, payload=dict(errors=errors))

    def delete_or_error(self):
        db.session.delete(self)

        try:
            db.session.commit()
        except IntegrityError:
            raise UnprocessableEntity('Could not delete requested entity.')
