
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
from sampleserve.users.auth import (
    auth_manager,
    bcrypt,
)

from sampleserve.models import (
    Sample,
    SampleValue,
    SiteMap,
    SiteMapWell,
    Client,
    Upload,
    Site,
    SiteData,
    Contact,
    ScheduleWellTests,
    Schedule,
    SubstanceGroup,
    Substance,
    Criteria,
    State,
    Test,
    TestMaterial,
    User,
    Role,
    Transaction,
    UserDeprecated,
    RoleDeprecated,
    Consultant,
    Manager,
    Company,
    Sampler,
    Office,
    Lab,
    Well,
    WellImage,
    Frequency,
)
from .views import (
    AdminModel,
    MyHomeView,
    UserView,
    SiteView,
    SampleView,
    SampleValueView,
    SubstanceView,
    LabView,
    OnboardLabView,
)
# from sampleserve.config import dev


def create_admin_app():
    app = Flask(__name__, template_folder="../templates")

    app.config.from_object('sampleserve.config.settings')

    db.init_app(app)
    bcrypt.init_app(app)
    auth_manager.init_app(app)

    # Create flask admin interface
    admin = Admin(index_view=MyHomeView(url='/'), template_mode='bootstrap3')
    admin.add_view(LabView(db.session, category="Users"))
    admin.add_view(OnboardLabView(name='Onboard Lab', category="Users"))
    admin.add_view(UserView(db.session, category="Users"))
    admin.add_view(AdminModel(Company, db.session, category="Users"))
    admin.add_view(AdminModel(Role, db.session, category="Users"))
    admin.add_view(SiteView(db.session, category="Sites"))
    admin.add_view(AdminModel(SiteMap, db.session, category="Sites"))
    admin.add_view(AdminModel(SiteMapWell, db.session, category="Sites"))
    admin.add_view(AdminModel(Client, db.session, category="Sites"))
    admin.add_view(AdminModel(SiteData, db.session, category="Sites"))
    admin.add_view(AdminModel(Contact, db.session, category="Sites"))
    admin.add_view(SampleView(db.session, category="Samples"))
    admin.add_view(SampleValueView(db.session, category="Samples"))
    admin.add_view(AdminModel(Upload, db.session, category="Uploads"))
    admin.add_view(AdminModel(Schedule, db.session, category="Schedules"))
    admin.add_view(SubstanceView(db.session, category="Substances"))
    admin.add_view(AdminModel(SubstanceGroup, db.session, category="Substances"))
    admin.add_view(AdminModel(ScheduleWellTests, db.session, category="Schedules"))
    admin.add_view(AdminModel(Criteria, db.session, category="Substances"))
    admin.add_view(AdminModel(State, db.session, category="States"))
    admin.add_view(AdminModel(Test, db.session, category="Tests"))
    admin.add_view(AdminModel(TestMaterial, db.session, category="Tests"))
    admin.add_view(AdminModel(Well, db.session, category="Wells"))
    admin.add_view(AdminModel(WellImage, db.session, category="Wells"))
    admin.init_app(app)

    return app
