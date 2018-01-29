
import json

from client import TestCase
from fixtures_states import data as states
from fixtures_companies import data as companies
from fixtures_labs import data as labs
from fixtures_sites import data as sites
from fixtures_schedules import data as schedules

from sampleserve.core import db
from sampleserve.users.models import (
    Company,
    Lab,
)
from sampleserve.substances.models import State
from sampleserve.sites.models import (
    Site,
    Schedule,
)


class SitesTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            self.create_user()

            for row in companies:
                db.session.add(Company(*row))

            for row in states:
                db.session.add(State(*row))

            for row in labs:
                db.session.add(Lab(*row))

            db.session.commit()

            for row in sites:
                db.session.add(Site(*row))

            db.session.commit()

            for row in schedules:
                db.session.add(Schedule(*row))

            db.session.commit()

    def test_index(self):
        rv = self.get_auth('/api/v1/sites/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_create_incomplete_unauthorized(self):
        rv = self.post_auth('/api/v1/sites/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 401

    def test_show_unauthorized(self):
        rv = self.get_auth('/api/v1/sites/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 401

    def test_edit_unauthorized(self):
        rv = self.patch_auth('/api/v1/sites/1', {'title': 'Site 1'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 401

    def test_delete_unauthorized(self):
        rv = self.delete_auth('/api/v1/sites/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 401
