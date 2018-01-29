
import json

from client import TestCase
from fixtures_states import data as states
from fixtures_companies import data as companies
from fixtures_labs import data as labs
from fixtures_sites import data as sites
from fixtures_substance_groups import data as substance_groups
from fixtures_substances import data as substances
from fixtures_wells import data as wells
from fixtures_schedules import data as schedules
from fixtures_samples import data as samples
from fixtures_sample_values import data as sample_values

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
from sampleserve.substances.models import (
    SubstanceGroup,
    Substance,
)
from sampleserve.wells.models import Well
from sampleserve.samples.models import (
    Sample,
    SampleValue,
)


class SamplesTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            for row in labs:
                db.session.add(Lab(*row))

            db.session.commit()

            for row in companies:
                db.session.add(Company(*row))

            db.session.commit()

            for row in states:
                db.session.add(State(*row))

            db.session.commit()

            for row in sites:
                db.session.add(Site(*row))

            db.session.commit()

            for row in substance_groups:
                db.session.add(SubstanceGroup(*row))

            db.session.commit()

            for row in substances:
                db.session.add(Substance(*row))

            for row in wells:
                db.session.add(Well(*row))

            for row in schedules:
                db.session.add(Schedule(*row))

            db.session.commit()

            for row in samples:
                db.session.add(Sample(*row))

            db.session.commit()

            for row in sample_values:
                db.session.add(SampleValue(*row))

            db.session.commit()

    def test_index(self):
        rv = self.client.get('/api/v1/samples/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_create_incomplete(self):
        rv = self.post('/api/v1/samples/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422

    def test_show(self):
        rv = self.client.get('/api/v1/samples/3', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_edit(self):
        rv = self.patch('/api/v1/samples/3', {'active': False}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['active'] == False

    def test_delete(self):
        rv = self.client.delete('/api/v1/samples/3', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 204
