"""

A handful of data validators for preprocessing requests:

    get_current_lab: Makes the current Lab object available on `g.current_lab`
    get_current_role: For authorization, adds the user's role name to `g.current_role`
    validate_json: Handles JSON parsing and errors, then puts JSON in `g.body`
    pagination_args: Looks for page and per_page in the query, returns capped integers.
    validate_schema: Raises appropriate errors on validating a JSON Schema agains a JSON body.

"""


import re
import os
import json
from functools import wraps

from flask import (
    abort,
    request,
    g,
)
from flask_login import current_user
import jsonschema
from werkzeug.exceptions import BadRequest as FlaskBadRequest

from sampleserve.users.models import Lab
from .errors import (
    UnprocessableEntity,
    BadRequest,
)

ADDITIONAL_PROPERTIES_RE = r"Additional properties are not allowed \(u?'(.*?)'.*?unexpected\)"
REQUIRED_PROPERTIES_RE = r"'(.*?)' is a required property"


def get_current_lab(f):
    @wraps(f)
    def decorator(lab_id, *args, **kwargs):
        lab = Lab.query.filter_by(url=lab_id).first()

        if lab:
            g.current_lab = lab
            return f(*args, **kwargs)

        return abort(404)
    return decorator


def get_current_role(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if current_user.is_anonymous:
            g.current_role = 'Anonymous'
        else:
            if current_user.role and current_user.role.name:
                g.current_role = current_user.role.name
            else:
                g.current_role = 'Unknown'

        return f(*args, **kwargs)
    return decorator


def validate_json(f):
    """Wrapper to validate JSON in the body of a request, raising appropriate HTTP errors.

    Only applies to POST and PATCH requests. Adds the validated JSON object to
    g.body.

    Raises: BadRequest
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        if request.method in ['POST', 'PATCH']:
            if not request.is_json:
                raise BadRequest('Request must be application/json.')

            try:
                g.body = request.get_json()
            except FlaskBadRequest:
                raise BadRequest('Problems parsing JSON.')
        return f(*args, **kwargs)
    return decorator


def pagination_args(page=1, per_page=400, max_per_page=400):
    """Parse pagination args from a request, raising appropriate HTTP errors.

    Arguments:
        page (int): Which page to return, default 1
        per_page (int): How many items per page, default 30
        max_per_page (int): Max items per page, default 100

    Returns: page, per_page (int, int)
    Raises: UnprocessableEntity
    """
    try:
        page = int(request.args.get('page', page))
        per_page = min(max_per_page, int(request.args.get('per_page', per_page)))
    except ValueError:
        raise UnprocessableEntity('Page and per_page must be integers.')

    return page, per_page


def validate_schema(document, schema):
    """Validate a JSON object against a JSON Schema, raising appropriate HTTP errors.

    Validation docs: http://json-schema.org/latest/json-schema-validation.html
    Nice test tool: http://www.jsonschemavalidator.net/
    Nice JSON schema generating tool: http://jsonschema.net/#/

    Arguments:
        document (object): A JSON object to validate
        schema (object): A JSON Schema to validate against

    Returns: None
    Raises: UnprocessableEntity
    """
    try:
        jsonschema.validate(document, schema)
    except jsonschema.exceptions.ValidationError as error:
        errors = []
        msg = 'Validation failed.'

        if error.absolute_schema_path[0] == 'properties':
            errors.append(dict(
                key=error.path[0],
                validator=error.validator,
            ))
        elif error.validator == 'required':
            required = re.match(REQUIRED_PROPERTIES_RE, error.message)
            key = required.group(1)
            msg = 'Missing one or more required properties.'
            errors.append(dict(
                key=key,
                validator=error.validator,
            ))
        elif error.validator == 'additionalProperties':
            additional = re.match(ADDITIONAL_PROPERTIES_RE, error.message)
            key = additional.group(1)
            msg = 'Additional properties are not allowed.'
            errors.append(
                dict(
                    key=key,
                    validator=error.validator,
                )
            )

        raise UnprocessableEntity(msg, payload=dict(errors=errors))
