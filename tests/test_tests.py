
import json

from client import TestCase
from fixtures_states import data as states
from fixtures_tests import data as tests
from fixtures_labs import data as labs
from fixtures_test_materials import data as test_materials

from sampleserve.core import db
from sampleserve.substances.models import State
from sampleserve.users.models import (
    Lab,
)
from sampleserve.tests.models import (
    Test,
    TestMaterial,
)


class TestsTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            for row in labs:
                db.session.add(Lab(*row))

            db.session.commit()

            for row in states:
                db.session.add(State(*row))

            db.session.commit()

            for row in tests:
                db.session.add(Test(*row))

            db.session.commit()

            for row in test_materials:
                db.session.add(TestMaterial(*row))

            db.session.commit()

    def test_index(self):
        rv = self.client.get('/api/v1/tests/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        rv = self.client.get('/api/v1/testmaterials/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_create_incomplete(self):
        rv = self.post('/api/v1/tests/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422
        rv = self.post('/api/v1/testmaterials/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422

    def test_show(self):
        rv = self.client.get('/api/v1/tests/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        rv = self.client.get('/api/v1/testmaterials/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_edit(self):
        rv = self.patch('/api/v1/tests/1', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['title'] == 'Test'
        rv = self.patch('/api/v1/testmaterials/1', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['title'] == 'Test'

    def test_delete(self):
        rv = self.client.delete('/api/v1/tests/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 204
        rv = self.client.delete('/api/v1/testmaterials/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 204
