

import types
from sqlalchemy import inspect

from sampleserve.substances.models import (
    SubstanceGroup,
    Substance,
    Criteria,
    State,
)

from sampleserve.wells.models import (
    Well,
    WellImage,
    Frequency,
)

from sampleserve.samples.models import (
    Sample,
    SampleValue,
)

from sampleserve.sites.models import (
    Site,
    Project,
    Schedule,
)

from sampleserve.users.models import (
    User,
    Role,
    Company,
    Consultant,
    Manager,
    Sampler,
    Office,
    Lab,
)

from sampleserve.tests.models import (
    Test,
    TestMaterial,
)

from sampleserve.sitemaps.models import (
    SiteMap,
    SiteMapWell,
)

from sampleserve.core import db, BaseModel
from sampleserve.app import create_app
# updated_on = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


app = create_app(config_filename='config/local.py')
objects = [SubstanceGroup, Substance, Criteria, State, Well, WellImage, Frequency, Sample, SampleValue, Site, Client, Schedule, User, Role, Company, Consultant, Manager, Sampler, Office, Lab, Test, TestMaterial, SiteMap, SiteMapWell]


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


with app.test_request_context():
    import os
    print(os.path.dirname(os.path.abspath(__file__)))
    print("running")
    basepath = "tests/helpers/"
    for o in objects:
        filepath = basepath + o._cached_tablename + ".py"
        with open(filepath, 'w') as file:
            results = o.query.filter_by().order_by(o.id).all()
            header = "\n" + o._cached_tablename + " = " + "[\n"
            file.write(header)
            for r in results:
                obj = object_as_dict(r)
                # obj.update(dict(_id=obj['id']))
                # obj.setdefault('id')
                file.write('    (%i, ' % obj['id'] + str(obj) + '),\n')
            footer = "]\n"
            file.write(footer)
            file.close()




















