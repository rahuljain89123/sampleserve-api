
import json

from flask import g

from client import NoDbTestCase

from sampleserve.rest.errors import (
    UnprocessableEntity,
    BadRequest,
)

from sampleserve.rest.validators import (
    validate_json,
    pagination_args,
)

def f():
    pass

decorator = validate_json(f)

class ValidatorsCase(NoDbTestCase):
    def test_missing_content_type_on_post(self):
        with self.app.test_request_context('/', method='POST', data=json.dumps({'a': 1})):
            with self.assertRaises(BadRequest):
                decorator()

    def test_json_on_post(self):
        with self.app.test_request_context('/', method='POST', data=json.dumps({'a': 1}),
                                           content_type='application/json'):
            decorator()
            assert g.body['a'] == 1

    def test_validate_json_on_post(self):
        with self.app.test_request_context('/', method='POST', data='{"badjson',
                                           content_type='application/json'):
            with self.assertRaises(BadRequest):
                decorator()

    def test_validate_json_on_patch(self):
        with self.app.test_request_context('/', method='PATCH', data='{"badjson',
                                           content_type='application/json'):
            with self.assertRaises(BadRequest):
                decorator()


class PaginationCase(NoDbTestCase):
    def test_valid_pagination(self):
        with self.app.test_request_context('/?page=2&per_page=10'):
            page, per_page = pagination_args()

            assert page == 2
            assert per_page == 10

    def test_default_pagination(self):
        with self.app.test_request_context('/'):
            page, per_page = pagination_args()

            assert page == 1
            assert per_page == 30

    def test_limit_pagination(self):
        with self.app.test_request_context('/?per_page=10'):
            page, per_page = pagination_args(max_per_page=3)

            assert page == 1
            assert per_page == 3

    def test_invalid_page(self):
        with self.app.test_request_context('/?page=a'):
            with self.assertRaises(UnprocessableEntity):
                page, per_page = pagination_args()

    def test_invalid_per_page(self):
        with self.app.test_request_context('/?per_page=a'):
            with self.assertRaises(UnprocessableEntity):
                page, per_page = pagination_args()
