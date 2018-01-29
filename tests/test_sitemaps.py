
import json

from client import TestCase
from fixtures_states import data as states
from fixtures_companies import data as companies
from fixtures_labs import data as labs
from fixtures_sites import data as sites
from fixtures_wells import data as wells
from fixtures_sitemaps import data as sitemaps
from fixtures_sitemap_wells import data as sitemap_wells

from sampleserve.core import db
from sampleserve.users.models import (
    Company,
    Lab,
)
from sampleserve.substances.models import State
from sampleserve.sites.models import Site
from sampleserve.wells.models import Well
from sampleserve.sitemaps.models import (
    SiteMap,
    SiteMapWell,
)


class SitemapsTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            for row in labs:
                db.session.add(Lab(*row))

            db.session.commit()

            for row in companies:
                db.session.add(Company(*row))

            for row in states:
                db.session.add(State(*row))

            db.session.commit()

            for row in sites:
                db.session.add(Site(*row))

            db.session.commit()

            for row in wells:
                db.session.add(Well(*row))

            db.session.commit()

            for row in sitemaps:
                db.session.add(SiteMap(*row))

            db.session.commit()

            for row in sitemap_wells:
                db.session.add(SiteMapWell(*row))

            db.session.commit()

    def test_index(self):
        rv = self.client.get('/api/v1/sitemaps/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        rv = self.client.get('/api/v1/sitemapwells/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_create_incomplete(self):
        rv = self.post('/api/v1/sitemaps/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422
        rv = self.post('/api/v1/sitemapwells/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422

    def test_show(self):
        rv = self.client.get('/api/v1/sitemaps/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        rv = self.client.get('/api/v1/sitemapwells/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_edit_incomplete(self):
        rv = self.patch('/api/v1/sitemaps/1', {'height': 700, 'width': 600}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['height'] == 700
        assert data['width'] == 600
        rv = self.patch('/api/v1/sitemapwells/1', {'xpos': 200, 'ypos': 300}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['xpos'] == 200
        assert data['ypos'] == 300

    def test_delete(self):
        rv = self.client.delete('/api/v1/sitemaps/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 204
        rv = self.client.get('/api/v1/sitemapwells/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 404
