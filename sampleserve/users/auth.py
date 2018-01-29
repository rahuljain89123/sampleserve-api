
from flask import Blueprint, g, jsonify, session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from sampleserve.emails.emails import reset_password
from sampleserve.rest.errors import UnprocessableEntity
from sampleserve.util import id_generator
from sampleserve.rest.validators import (
    validate_json,
    validate_schema,
    get_current_lab,
    get_current_role,
)

from . import schemas
from .models import User, Role

auth = Blueprint('auth', __name__)
auth_manager = LoginManager()
bcrypt = Bcrypt()


@auth_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/signin', methods=['POST'], subdomain='<lab_id>')
@validate_json
@get_current_lab
def signin():
    validate_schema(g.body, schemas.signin)

    user = User.query.filter_by(lab=g.current_lab, email=g.body['email']).first()
    if user and bcrypt.check_password_hash(user.password, g.body['password']):
        login_user(user)
        return jsonify(success=True)

    return jsonify(success=False)


@auth.route('/signout', methods=['POST'], subdomain='<lab_id>')
@login_required
@get_current_lab
def signout():
    logout_user()
    return jsonify(success=True)


@auth.route('/reset', methods=['POST'], subdomain='<lab_id>')
@validate_json
@get_current_lab
def reset():
    validate_schema(g.body, schemas.reset)

    if 'email' in g.body:
        user = User.query.filter_by(lab=g.current_lab, email=g.body['email']).first()

        if user:
            user.reset_code = id_generator()
            user.save_or_error()

            reset_password(user)

            return jsonify(success=True)
    elif 'reset_code' in g.body and 'password' in g.body:
        user = User.query.filter_by(lab=g.current_lab, reset_code=g.body['reset_code']).first()

        if user:
            user.reset_code = None
            user.password = bcrypt.generate_password_hash(g.body['password'])
            user.save_or_error()
            login_user(user)
            return jsonify(success=True)

    return jsonify(success=False)


@login_required
@get_current_lab
def get_user():
    return jsonify(current_user.json())


@get_current_lab
def get_lab():
    return jsonify(g.current_lab.json())
