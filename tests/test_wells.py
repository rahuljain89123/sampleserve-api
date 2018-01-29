
import json

from client import TestCase
from fixtures_wells import data
from fixtures_well_images import data as well_images
from fixtures_labs import data as labs
from fixtures_frequencies import data as frequencies

from sampleserve.core import db
from sampleserve.users.models import (
    Lab,
)
from sampleserve.wells.models import (
    Well,
    WellImage,
    Frequency,
)


class WellsTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            for row in labs:
                db.session.add(Lab(*row))

            db.session.commit()

            for row in data:
                db.session.add(Well(*row))

            db.session.commit()

            for row in well_images:
                db.session.add(WellImage(*row))

            for row in frequencies:
                db.session.add(Frequency(*row))

            db.session.commit()

    def test_index(self):
        rv = self.client.get('/api/v1/wells/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_create_incomplete(self):
        rv = self.post('/api/v1/wells/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422

    def test_show(self):
        rv = self.client.get('/api/v1/wells/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_edit(self):
        rv = self.patch('/api/v1/wells/1', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['title'] == 'Test'

    def test_delete(self):
        rv = self.client.delete('/api/v1/wells/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 204
