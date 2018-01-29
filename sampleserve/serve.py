
"""

Entry point for the Flask CLI. Creates the app and serves it, also implements other
CLI commands like initdb, dropdb and populatedb. Right now, it pulls example data
from the test fixtures, but in the future it could load a db dump instead.

"""

import sys
import os

import click
import datetime

from flask import Flask, session, url_for, jsonify
from alembic import op
import sqlalchemy as sa

from sampleserve.substances.models import (
    SubstanceGroup,
    Substance,
    Criteria,
    CriteriaValues,
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
    SiteData,
    Client,
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

from sampleserve.app import create_app
from sampleserve.core import db
from sampleserve.users.auth import bcrypt
from sampleserve.reports.helpers import getSitemapInfo


app = create_app()


@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Done creating models.')


@app.cli.command()
def dropdb():
    db.reflect()
    db.drop_all()
    click.echo('Done dropping models.')


def addRowsToDatabase(fixture, model):
    for r in fixture:
        m = model()
        for key, value in r[1].iteritems():
            setattr(m, key, value)
        db.session.add(m)
    db.session.commit()


def addUnkeyedRowsToDatabase(fixture, model):
    for r in fixture:
        m = model()
        for key, value in r.iteritems():
            setattr(m, key, value)
        db.session.add(m)
    db.session.commit()


def createCriteriaValues(criteria_values):
    # Populate criteria values
    for cv in criteria_values:
        obj = CriteriaValues(
            criteria_id=cv['criteria_id'],
            substance_id=cv['substance_id'],
            value=cv['value'])
        db.session.add(obj)
    db.session.commit()


@app.cli.command()
def populatedb():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tests', 'helpers'))

    from sampleserve.fixtures.company import company
    from sampleserve.fixtures.consultant import consultant
    from sampleserve.fixtures.criteria import criteria
    from sampleserve.fixtures.criteria_values import criteria_values
    from sampleserve.fixtures.frequency import frequency
    from sampleserve.fixtures.lab import lab
    from sampleserve.fixtures.manager import manager
    from sampleserve.fixtures.office import office
    from sampleserve.fixtures.client import client
    from sampleserve.fixtures.role import role
    from sampleserve.fixtures.sample import sample
    from sampleserve.fixtures.sample_value import sample_value
    from sampleserve.fixtures.sampler import sampler
    from sampleserve.fixtures.schedule import schedule
    from sampleserve.fixtures.site import site
    from sampleserve.fixtures.site_map_well import site_map_well
    from sampleserve.fixtures.site_map import site_map
    from sampleserve.fixtures.state import state
    from sampleserve.fixtures.substance import substance
    from sampleserve.fixtures.substance_group import substance_group
    from sampleserve.fixtures.test import test
    from sampleserve.fixtures.test_material import test_material
    from sampleserve.fixtures.well import well
    from sampleserve.fixtures.well_image import well_image

    addRowsToDatabase(lab, Lab)
    addRowsToDatabase(state, State)
    # addRowsToDatabase(company, Company)
    # addRowsToDatabase(client, Client)
    # addRowsToDatabase(site, Site)
    # addRowsToDatabase(consultant, Consultant)
    addRowsToDatabase(criteria, Criteria)
    addRowsToDatabase(frequency, Frequency)
    # addRowsToDatabase(manager, Manager)
    # addRowsToDatabase(office, Office)
    addRowsToDatabase(role, Role)
    # addRowsToDatabase(schedule, Schedule)
    addUnkeyedRowsToDatabase(substance_group, SubstanceGroup)
    addUnkeyedRowsToDatabase(substance, Substance)
    addRowsToDatabase(test, Test)
    addRowsToDatabase(test_material, TestMaterial)
    # addRowsToDatabase(well, Well)
    # addRowsToDatabase(well_image, WellImage)
    # addRowsToDatabase(sample, Sample)
    # addRowsToDatabase(sample_value, SampleValue)
    # addRowsToDatabase(sampler, Sampler)
    # addRowsToDatabase(site_map, SiteMap)
    # addRowsToDatabase(site_map_well, SiteMapWell)

    # Updates the database to fix primary keys after importing
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('company', 'id'), (SELECT MAX(id) FROM company)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('consultant', 'id'), (SELECT MAX(id) FROM consultant)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('criteria', 'id'), (SELECT MAX(id) FROM criteria)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('frequency', 'id'), (SELECT MAX(id) FROM frequency)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('lab', 'id'), (SELECT MAX(id) FROM lab)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('manager', 'id'), (SELECT MAX(id) FROM manager)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('office', 'id'), (SELECT MAX(id) FROM office)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('client', 'id'), (SELECT MAX(id) FROM client)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('role', 'id'), (SELECT MAX(id) FROM role)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('sample', 'id'), (SELECT MAX(id) FROM sample)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('sample_value', 'id'), (SELECT MAX(id) FROM sample_value)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('sampler', 'id'), (SELECT MAX(id) FROM sampler)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('schedule', 'id'), (SELECT MAX(id) FROM schedule)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('site', 'id'), (SELECT MAX(id) FROM site)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('site_map_well', 'id'), (SELECT MAX(id) FROM site_map_well)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('site_map', 'id'), (SELECT MAX(id) FROM site_map)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('state', 'id'), (SELECT MAX(id) FROM state)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('substance', 'id'), (SELECT MAX(id) FROM substance)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('substance_group', 'id'), (SELECT MAX(id) FROM substance_group)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('test', 'id'), (SELECT MAX(id) FROM test)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('test_material', 'id'), (SELECT MAX(id) FROM test_material)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('transaction', 'id'), (SELECT MAX(id) FROM transaction)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('well', 'id'), (SELECT MAX(id) FROM well)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('well_image', 'id'), (SELECT MAX(id) FROM well_image)+1)")
    db.session.execute("SELECT pg_catalog.setval(pg_get_serial_sequence('well_options', 'id'), (SELECT MAX(id) FROM well_options)+1)")

    # Populate criteria values
    createCriteriaValues(criteria_values)

    # Create Sampleserve Admin
    user = User(
        email="admin@nickwoodhams.com",
        password=bcrypt.generate_password_hash("admin"),
        name="Sampleserve Mr. Admin",
        phone="123-456-7890",
        role_id=1,
        active=True,
        lab_id=0,
    )
    db.session.add(user)
    db.session.commit()

    # Create LabAdmin
    user = User(
        email="labadmin@nickwoodhams.com",
        password=bcrypt.generate_password_hash("labadmin"),
        name="Mr. LabAdmin",
        phone="123-456-7890",
        role_id=2,
        active=True,
        lab_id=0,
    )
    db.session.add(user)
    db.session.commit()

    # Create LabAssociate
    user = User(
        email="labassociate@nickwoodhams.com",
        password=bcrypt.generate_password_hash("labassociate"),
        name="Mr. LabAssociate",
        phone="123-456-7890",
        role_id=3,
        active=True,
        lab_id=0,
    )
    db.session.add(user)
    db.session.commit()

    # Create a new Client for the Lab, ie "Company"
    company = Company(title="Test Company, Inc.", active=True, lab_id=0)
    db.session.add(company)
    db.session.commit()

    # Create CompanyAdmin
    user = User(
        email="companyadmin@nickwoodhams.com",
        password=bcrypt.generate_password_hash("companyadmin"),
        name="Mr. CompanyAdmin",
        phone="123-456-7890",
        role_id=4,
        active=True,
        lab_id=0,
        companies=[company],
    )
    db.session.add(user)
    db.session.commit()

    # Create CompanyAssociate
    user = User(
        email="companyassociate@nickwoodhams.com",
        password=bcrypt.generate_password_hash("companyassociate"),
        name="Mr. CompanyAssociate",
        phone="123-456-7890",
        role_id=5,
        active=True,
        lab_id=0,
        companies=[company],
    )
    db.session.add(user)
    db.session.commit()

    # Create a Client
    client = Client(
        company_id=company.id,
        name="Test Client"
    )
    db.session.add(client)
    db.session.commit()

    # Create a Site
    site = Site(
        title="Test Site",
        company_id=company.id,
        client_id=client.id,
        lab_id=0,
        city="Kalamazoo",
        state_id=35,
        state="Michigan",
    )
    db.session.add(site)
    db.session.commit()

    # Create associated Site Data for the site
    site_data = SiteData(site_id=site.id)
    db.session.add(site_data)
    db.session.commit()

    # Create ClientManager
    user = User(
        email="clientmanager@nickwoodhams.com",
        password=bcrypt.generate_password_hash("clientmanager"),
        name="Mr. ClientManager",
        phone="123-456-7890",
        role_id=6,
        active=True,
        lab_id=0,
        companies=[company],
        clients=[client],
    )
    db.session.add(user)
    db.session.commit()

    # Create Technician
    user = User(
        email="technician@nickwoodhams.com",
        password=bcrypt.generate_password_hash("technician"),
        name="Mr. Technician",
        phone="123-456-7890",
        role_id=7,
        active=True,
        lab_id=0,
        sites=[site],
    )
    db.session.add(user)
    db.session.commit()

    # Create Technician
    user = User(
        email="schindler@sampleserve.com",
        password=bcrypt.generate_password_hash("sampleserve69*"),
        name="Russell Schindler",
        phone="231-218-7955",
        role_id=4,
        active=True,
        lab_id=0,
        companies=[company],
    )
    db.session.add(user)
    db.session.commit()

    # Create a sitedata object for each site
    sites = Site.query.filter_by().all()
    for site in sites:
        site_data = SiteData(site_id=site.id)
        db.session.add(site_data)
    db.session.commit()

    click.echo('Done populating db.')


@app.cli.command()
def list_routes():
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)


@app.cli.command()
def cleanup_substances():
    substances = Substance.query.filter_by().all()
    for s in substances:
        cas = s.cas
        s.cas = ' '
        db.session.commit()
        s.cas = cas
        db.session.commit()


@app.cli.command()
def populate_criteria_values():
    from sampleserve.fixtures.criteria_values import criteria_values
    # Populate criteria values
    createCriteriaValues(criteria_values)


@app.cli.command()
def update_sitemap_urls():
    sitemaps = SiteMap.query.filter_by().all()
    for sm in sitemaps:
        sm_info = getSitemapInfo(sm.id)
        sm.url = sm_info['public_url']
        db.session.commit()


@app.cli.command()
def own_all_sites():
    sites = Site.query.filter_by().all()
    for s in sites:
        s.client_id = 3
        s.company_id = 53
        s.lab_id = 0
        db.session.commit()
