
import json

from flask_login import current_user

from client import TestCase, NoDbTestCase
from fixtures_consultants import data as consultants
from fixtures_managers import data as managers
from fixtures_companies import data as companies
from fixtures_states import data as states
from fixtures_sites import data as sites
from fixtures_samplers import data as sampler
from fixtures_offices import data as offices
from fixtures_labs import data as labs
from fixtures_roles import data as roles

from sampleserve.rest.errors import UnprocessableEntity
from sampleserve.rest.validators import validate_schema

from sampleserve.core import db
from sampleserve.users import schemas as users_schemas
from sampleserve.users.auth import bcrypt
from sampleserve.substances.models import State
from sampleserve.sites.models import Site
from sampleserve.users.models import (
    User,
    Role,
    Consultant,
    Manager,
    Company,
    Sampler,
    Office,
    Lab,
)


class UsersTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            for row in consultants:
                db.session.add(Consultant(*row))

            for row in managers:
                db.session.add(Manager(*row))

            for row in companies:
                db.session.add(Company(*row))

            for row in sampler:
                db.session.add(Sampler(*row))

            for row in offices:
                db.session.add(Office(*row))

            for row in states:
                db.session.add(State(*row))

            db.session.commit()

            for row in labs:
                db.session.add(Lab(*row))

            db.session.commit()

            for row in sites:
                db.session.add(Site(*row))

            for row in roles:
                db.session.add(Role(*row))

            db.session.commit()

    def test_index(self):
        rv = self.client.get('/api/v1/consultants/', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_create_incomplete(self):
        rv = self.post('/api/v1/consultants/', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 422

    def test_show(self):
        rv = self.client.get('/api/v1/consultants/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200

    def test_edit(self):
        rv = self.patch('/api/v1/consultants/1', {'title': 'Test'}, base_url='http://test.sampleserve.dev')
        assert rv.status_code == 200
        data = json.loads(rv.data)
        assert data['title'] == 'Test'

    def test_delete(self):
        rv = self.client.delete('/api/v1/consultants/1', base_url='http://test.sampleserve.dev')
        assert rv.status_code == 204


class UsersTestCase(TestCase):
    def setUp(self):
        with self.app.app_context():
            for row in labs:
                db.session.add(Lab(*row))

            for row in roles:
                db.session.add(Role(*row))

            db.session.commit()

    def test_signin(self):
        self.create_user()
        with self.client as c:
            p = {'email': 'guatguat@example.com', 'password': 'guatguat'}
            rv = c.post(
                '/api/v1/auth/signin',
                data=json.dumps(p),
                content_type='application/json',
                base_url='http://test.sampleserve.dev'
            )
            assert rv.status_code == 200
            assert current_user.id == self.user_id

    def test_signout(self):
        self.create_user()
        with self.client as c:
            p = {'email': 'guatguat@example.com', 'password': 'guatguat'}
            rv = c.post(
                '/api/v1/auth/signin',
                data=json.dumps(p),
                content_type='application/json',
                base_url='http://test.sampleserve.dev'
            )
            assert rv.status_code == 200
            assert current_user.id == self.user_id
            c.post('/api/v1/auth/signout', base_url='http://test.sampleserve.dev')
            assert current_user.is_anonymous

    def test_signup(self):
        with self.client as c:
            p = {'email': 'guat@example.com', 'password': 'guat'}
            rv = c.post(
                '/api/v1/users/',
                data=json.dumps(p),
                content_type='application/json',
                base_url='http://test.sampleserve.dev'
            )
            rv = json.loads(rv.data)
            p = {'email': 'guat@example.com', 'password': 'guat'}
            c.post(
                '/api/v1/auth/signin',
                data=json.dumps(p),
                content_type='application/json',
                base_url='http://test.sampleserve.dev'
            )
            assert current_user.id == rv['id']

    def test_invite(self):
        with self.client as c:
            p = {'email': 'guat@example.com', 'role_id': 2}
            rv = c.post(
                '/api/v1/users/',
                data=json.dumps(p),
                content_type='application/json',
                base_url='http://test.sampleserve.dev'
            )
            rv = json.loads(rv.data)
            p = {'password': 'guat'}
            c.patch(
                '/api/v1/users/{}'.format(rv['id']),
                data=json.dumps(p),
                content_type='application/json',
                base_url='http://test.sampleserve.dev'
            )
            p = {'email': 'guat@example.com', 'password': 'guat'}
            c.post(
                '/api/v1/auth/signin',
                data=json.dumps(p),
                content_type='application/json',
                base_url='http://test.sampleserve.dev'
            )
            assert current_user.id == rv['id']

class UsersSchemasTestCase(NoDbTestCase):
    def test_valid_signup(self):
        valid = {'email': 'guatguat@example.com', 'password': 'guatguat'}
        validate_schema(valid, users_schemas.signup)

    def test_valid_signin(self):
        valid = {'email': 'guatguat@example.com', 'password': 'guatguat'}
        validate_schema(valid, users_schemas.signin)

    def test_invalid_length(self):
        invalid = {'email': 'guatguat@example.com', 'password': 'gua'}
        with self.assertRaises(UnprocessableEntity):
            validate_schema(invalid, users_schemas.signup)

    def test_invalid_email(self):
        invalid = {'email': 'guat', 'password': 'guat'}
        with self.assertRaises(UnprocessableEntity):
            validate_schema(invalid, users_schemas.signup)

    def test_valid_email(self):
        invalid = {'email': 'guatguat@example.com', 'password': 'guat'}
        validate_schema(invalid, users_schemas.signup)

    def test_invalid_additional_key(self):
        invalid = {'password': 'guatguat', 'active': True}
        with self.assertRaises(UnprocessableEntity):
            validate_schema(invalid, users_schemas.signup)

    def test_invalid_multiple_additional_keys(self):
        invalid = {'password': 'guatguat', 'active': True, 'test': True}
        with self.assertRaises(UnprocessableEntity):
            validate_schema(invalid, users_schemas.signup)
