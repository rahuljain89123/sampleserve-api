
import json

from client import TestCase
from fixtures_substance_groups import data as substance_groups
from fixtures_labs import data as labs
from fixtures_states import data as states
from fixtures_criteria import data as criteria
from fixtures_substances import data as substances
from fixtures_criteria_values import data as criteria_values

from sampleserve.core import db
from sampleserve.users.models import (
    Lab,
)
from sampleserve.substances.models import (
    SubstanceGroup,
    Substance,
    Criteria,
    State,
)


class SubstancesTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            for row in labs:
                db.session.add(Lab(*row))

            db.session.commit()

            for row in substance_groups:
                db.session.add(SubstanceGroup(*row))

            for row in states:
                db.session.add(State(*row))

            db.session.commit()

            for row in criteria:
                db.session.add(Criteria(*row))

            db.session.commit()

            for row in substances:
                db.session.add(Substance(*row))

            db.session.commit()

    def test_index(self):
        rv = self.client.get('/api/v1/substances/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_create_incomplete(self):
        rv = self.post('/api/v1/substances/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422

    def test_show(self):
        rv = self.client.get('/api/v1/substances/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_edit(self):
        rv = self.patch('/api/v1/substances/1', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['title'] == 'Test'

    def test_delete(self):
        rv = self.client.delete('/api/v1/substances/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 204
