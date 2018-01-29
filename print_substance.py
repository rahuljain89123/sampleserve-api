
from sqlalchemy import inspect
from sampleserve.substances.models import (
    Substance
)
from sampleserve.core import db, BaseModel
from sampleserve.app import create_app


app = create_app(config_filename='config/local.py')


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


with app.test_request_context():
    results = Substance.query.filter_by().order_by(Substance.id).all()
    for r in results:
        print(r)
        print(object_as_dict(r).values())

















