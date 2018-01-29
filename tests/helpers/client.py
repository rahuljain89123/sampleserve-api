
import json
import os
import unittest

from flask_login import login_user

from sampleserve.app import create_app
from sampleserve.core import db
from sampleserve.users.auth import bcrypt
from sampleserve.users.models import User

config_file = 'config/docker.py'

if os.environ.get('CI'):
    config_file = 'config/circleci.py'

app = create_app(config_file)


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is not TestCase and cls.setUp is not TestCase.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                TestCase.setUp(self)
                return orig_setUp(self, *args, **kwargs)

            cls.setUp = setUpOverride

    def create_user(self):
        with self.app.app_context():
            user = User()
            user.email = 'guatguat@example.com',
            user.password = bcrypt.generate_password_hash('guatguat')
            user.active = True
            user.pending = False
            db.session.add(user)
            db.session.commit()
            self.user_id = user.id

    def get_auth(self, *args, **kwargs):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['_fresh'] = True
            return c.get(*args, **kwargs)

    def post_auth(self, *args, **kwargs):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['_fresh'] = True
            return c.post(
                args[0],
                data=json.dumps(args[1]),
                content_type='application/json',
                **kwargs
            )

    def patch_auth(self, *args, **kwargs):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['_fresh'] = True
            return c.patch(
                args[0],
                data=json.dumps(args[1]),
                content_type='application/json',
                **kwargs
            )

    def delete_auth(self, *args, **kwargs):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['_fresh'] = True
            return c.delete(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.client.post(
            args[0],
            data=json.dumps(args[1]),
            content_type='application/json',
            **kwargs
        )

    def patch(self, *args, **kwargs):
        return self.client.patch(
            args[0],
            data=json.dumps(args[1]),
            content_type='application/json',
            **kwargs
        )

    def setUp(self):
        with app.app_context():
            db.session.commit()
            db.drop_all()
            db.create_all()

        self.client = app.test_client()
        self.app = app

    def tearDown(self):
        with app.app_context():
            db.session.commit()
            db.drop_all()


class NoDbTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is not NoDbTestCase and cls.setUp is not NoDbTestCase.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                NoDbTestCase.setUp(self)
                return orig_setUp(self, *args, **kwargs)

            cls.setUp = setUpOverride

    def post(self, *args):
        return self.client.post(
            args[0],
            data=json.dumps(args[1]),
            content_type='application/json'
        )

    def patch(self, *args):
        return self.client.patch(
            args[0],
            data=json.dumps(args[1]),
            content_type='application/json'
        )

    def setUp(self):
        self.client = app.test_client()
        self.app = app

    def tearDown(self):
        pass
