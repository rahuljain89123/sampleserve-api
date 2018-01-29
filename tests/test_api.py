
from client import TestCase


class APITestCase(TestCase):
    def test_get(self):
        rv = self.client.get('/api/v1/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
