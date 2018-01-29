
"""

Flask app factory. Create the app and attach all libraries with create_app.
Also takes care of registering all routes, including API views.

Handles a couple of different config scenarios, including Docker, CircleCI and testing.

"""

import httplib
import wtforms_json

from flask import Flask
from flask_cors import CORS
from flask_admin import Admin, BaseView, AdminIndexView, expose
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from raven.contrib.flask import Sentry

from sampleserve.core import db
from sampleserve.v1 import (
    api,
    auth,
    labs,
    bplabs,
    roles,
    samples,
    uploads,
    substancegroups,
    substances,
    criterias,
    states,
    sites,
    sitedata,
    clients,
    schedules,
    schedulewelltests,
    contacts,
    users,
    get_user,
    get_lab,
    consultants,
    companies,
    managers,
    samplers,
    offices,
    wells,
    wellimages,
    frequencies,
    reports,
    imports,
    tests,
    testmaterials,
    sitemaps,
    sitemapwells,
)

from sampleserve.users.auth import (
    auth_manager,
    bcrypt,
)

from sampleserve.rest.errors import (
    UnprocessableEntity,
    handle_unprocessable_entity,
    BadRequest,
    handle_bad_request,
    handle_unauthorized,
    handle_page_not_found,
    handle_method_not_allowed,
    BadUpload,
    handle_bad_upload,
    BadInvite,
    handle_bad_invite,
    FormError,
    handle_form_error,
)
from sampleserve import mail
from sampleserve.emails.helpers import firstname

from sampleserve.admin.views import AdminModel, MyHomeView, UserView, SiteView


def register_api(app, view, url, pk='id', pk_type='int', **kwargs):
    app.add_url_rule(url, defaults={pk: None}, view_func=view, methods=['GET'], **kwargs)
    app.add_url_rule(url, view_func=view, methods=['POST'], **kwargs)
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view, methods=['GET', 'PATCH', 'DELETE'], **kwargs)


def create_app():
    app = Flask(__name__)

    app.config.from_object('sampleserve.config.settings')

    # Turn off strict slashes
    app.url_map.strict_slashes = False

    # Initialize Flask_Mail
    mail.init_app(app)

    app.register_blueprint(api, url_prefix='/api/v1', subdomain='<lab_id>')
    app.register_blueprint(auth, url_prefix='/api/v1/auth', subdomain='<lab_id>')
    app.register_blueprint(reports, url_prefix='/api/v1/reports', subdomain='<lab_id>')
    app.register_blueprint(imports, url_prefix='/api/v1/imports', subdomain='<lab_id>')
    app.register_blueprint(bplabs, url_prefix='/api/v1/labs')

    register_api(app, labs, '/api/v1/labs/', subdomain='<lab_id>')
    register_api(app, roles, '/api/v1/roles/', subdomain='<lab_id>')
    register_api(app, samples, '/api/v1/samples/', subdomain='<lab_id>')
    register_api(app, substances, '/api/v1/substances/', subdomain='<lab_id>')
    register_api(app, substancegroups, '/api/v1/substancegroups/', subdomain='<lab_id>')
    register_api(app, substances, '/api/v1/substances/', subdomain='<lab_id>')
    register_api(app, criterias, '/api/v1/criterias/', subdomain='<lab_id>')
    register_api(app, states, '/api/v1/states/', subdomain='<lab_id>')
    register_api(app, sites, '/api/v1/sites/', subdomain='<lab_id>')
    register_api(app, sitedata, '/api/v1/sitedata/', subdomain='<lab_id>')
    register_api(app, clients, '/api/v1/clients/', subdomain='<lab_id>')
    register_api(app, uploads, '/api/v1/uploads/', subdomain='<lab_id>')
    register_api(app, schedules, '/api/v1/schedules/', subdomain='<lab_id>')
    register_api(app, schedulewelltests, '/api/v1/schedulewelltests/', subdomain='<lab_id>')
    register_api(app, contacts, '/api/v1/contacts/', subdomain='<lab_id>')
    register_api(app, users, '/api/v1/users/', subdomain='<lab_id>')
    register_api(app, consultants, '/api/v1/consultants/', subdomain='<lab_id>')
    register_api(app, companies, '/api/v1/companies/', subdomain='<lab_id>')
    register_api(app, managers, '/api/v1/managers/', subdomain='<lab_id>')
    register_api(app, samplers, '/api/v1/samplers/', subdomain='<lab_id>')
    register_api(app, offices, '/api/v1/offices/', subdomain='<lab_id>')
    register_api(app, wells, '/api/v1/wells/', subdomain='<lab_id>')
    register_api(app, wellimages, '/api/v1/wellimages/', subdomain='<lab_id>')
    register_api(app, frequencies, '/api/v1/frequencies/', subdomain='<lab_id>')
    register_api(app, tests, '/api/v1/tests/', subdomain='<lab_id>')
    register_api(app, testmaterials, '/api/v1/testmaterials/', subdomain='<lab_id>')
    register_api(app, sitemaps, '/api/v1/sitemaps/', subdomain='<lab_id>')
    register_api(app, sitemapwells, '/api/v1/sitemapwells/', subdomain='<lab_id>')

    app.add_url_rule('/api/v1/user', 'user', get_user, subdomain='<lab_id>')
    app.add_url_rule('/api/v1/lab', 'lab', get_lab, subdomain='<lab_id>')

    app.register_error_handler(UnprocessableEntity, handle_unprocessable_entity)
    app.register_error_handler(BadUpload, handle_bad_upload)
    app.register_error_handler(BadInvite, handle_bad_invite)
    app.register_error_handler(BadRequest, handle_bad_request)
    app.register_error_handler(httplib.NOT_FOUND, handle_page_not_found)
    app.register_error_handler(httplib.METHOD_NOT_ALLOWED, handle_method_not_allowed)
    app.register_error_handler(httplib.UNAUTHORIZED, handle_unauthorized)
    app.register_error_handler(FormError, handle_form_error)

    # register some custom app filters
    app.jinja_env.filters['firstname'] = firstname

    db.init_app(app)
    bcrypt.init_app(app)
    auth_manager.init_app(app)

    if app.config.get('DEBUG'):
        CORS(app, origins=app.config.get('CORS_SERVER_NAME'), supports_credentials=True)

    # Activate wtforms json helpers
    wtforms_json.init()

    # Activate sentry
    if not app.config.get('DEBUG'):
        sentry = Sentry(app, dsn='http://ded2865b70164ed58a18a82f3bc1d589:be268c2f50bd425f98acbe2e3f712317@sentry.nickwoodhams.com/19')

    return app
