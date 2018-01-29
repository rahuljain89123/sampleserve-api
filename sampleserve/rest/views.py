"""

Two base views for REST API endpoints for each data model: BaseView
and PrivateView. These views implement very basic operations of requests
on each model:

    GET - retrieve
    POST - create
    PATCH - update
    DELETE - delete

Each view has a couple of decorators attached to them by default, to validate
commnonly used parameters, or for attaching objects to the flask global `g`.

Flask docs for MethodView: http://flask.pocoo.org/docs/0.12/api/#flask.views.MethodView

Each view can be overriden by inheritence, with the same decorators available:

class CatView(BaseView):
    def post(self):
        if g.body['sound'] == 'woof':
            return abort(404)
        elif g.body['sound'] == 'meow':
            return { success: True }

"""

import httplib
from flask import (
    abort,
    jsonify,
    request,
    g,
)
from flask.views import MethodView
from flask_login import (
    login_required,
    current_user,
)

from sampleserve.rest.validators import (
    validate_json,
    get_current_lab,
    pagination_args,
    get_current_role,
)


class BaseView(MethodView):
    """Basic restful Flask class that handles get/post/patch/delete for data models.

    URL routes are attached via sampleserve.app.register_api, which attaches the
    following URLs/methods:

        /model ['GET', 'POST']
        /model/<id> ['GET', 'PATCH', 'DELETE']

    Validators:
        validate_json: Validates incoming JSON, which is available in `g.body`.
        get_current_lab: Puts current Lab object in `g.current_lab`
        get_current_role: Puts current Role name in `g.current_role`

    JSON is validated for all POST and PATCH calls.

    Each model can be authorized against the current_lab
    and the current_user by implementing the .is_authorized(current_lab, current_user)
    function.

    Each endpoint can be authorized against allowed roles, by using the class
    properties: get_roles, post_roles, patch_roles, delete_roles.

    GET requests for multiple items are automatically paginated with
    sampleserve.rest.validators.pagination_args.
    """
    decorators = [validate_json, get_current_lab, get_current_role]

    def get(self, id=None):
        """GET /model or GET /model/<id>

        The GET request can be either for a list of items, or a specific item, depending
        on whether <id> is specified.
        """
        q = self.model.query

        if hasattr(self.model, 'role_query'):
            q = self.model.role_query

        if id:
            instance = q.filter(getattr(self.model, self.model.__mapper__.primary_key[0].name) == id).first_or_404()

            if hasattr(self.model, 'is_authorized'):
                if not instance.is_authorized(g.current_lab, current_user):
                    abort(httplib.UNAUTHORIZED)

            if hasattr(self, 'get_roles'):
                if g.current_role not in self.get_roles and g.current_role != 'Admin':
                    abort(httplib.UNAUTHORIZED)

            res = instance.json()
            return jsonify(res)

        filters = request.args.keys()

        if filters:
            fields = self.model._fields()
            relations = self.model._relations()

            for query_filter in filters:
                if query_filter in fields:
                    q = q.filter(getattr(self.model, query_filter) == request.args.get(query_filter))
                elif query_filter in relations:
                    q = q.filter(getattr(self.model, query_filter).any(id=request.args.get(query_filter)))

        page, per_page = pagination_args()
        pagination = q.paginate(page, per_page, error_out=False)

        if not pagination.items:
            return jsonify([])

        res = [item.json() for item in pagination.items]
        return jsonify(res)

    def post(self):
        """POST /model

        Creates a new object of model, returning it as JSON with an `id` key.
        """
        if hasattr(self, 'post_roles'):
            if current_user.is_anonymous or not current_user.role:
                abort(httplib.UNAUTHORIZED)
            if current_user.role.name not in self.post_roles:
                abort(httplib.UNAUTHORIZED)

        instance = self.model()
        instance.patch(g.body)
        instance.save_or_error()
        res = instance.json()
        return jsonify(res)

    def patch(self, id):
        """PATCH /model/<id>

        Updates a model identified by `id`, returning the updating JSON.
        """
        instance = self.model.query.get_or_404(id)

        if hasattr(self.model, 'is_authorized'):
            if not instance.is_authorized(g.current_lab, current_user):
                abort(httplib.UNAUTHORIZED)

        if hasattr(self, 'patch_roles'):
            if current_user.is_anonymous or not current_user.role:
                abort(httplib.UNAUTHORIZED)
            if current_user.role.name not in self.patch_roles:
                abort(httplib.UNAUTHORIZED)

        instance.patch(g.body)
        instance.save_or_error()
        res = instance.json()
        return jsonify(res)

    def delete(self, id):
        """DELETE /model/<id>

        Deletes a model identified by `id`, returning no content.
        """
        instance = self.model.query.get_or_404(id)

        if hasattr(self.model, 'is_authorized'):
            if not instance.is_authorized(g.current_lab, current_user):
                abort(httplib.UNAUTHORIZED)

        if hasattr(self, 'delete_roles'):
            if current_user.is_anonymous or not current_user.role:
                abort(httplib.UNAUTHORIZED)
            if current_user.role.name not in self.delete_roles:
                abort(httplib.UNAUTHORIZED)

        instance.delete_or_error()
        return ('', httplib.NO_CONTENT)


class PrivateView(BaseView):
    """An idential view to BaseView, with the addition of login_required.
    """
    decorators = [validate_json, login_required, get_current_lab, get_current_role]
