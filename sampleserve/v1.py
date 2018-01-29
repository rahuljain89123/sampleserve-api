
"""

Since the API will support a mobile app alongside the web, it's important to
version lock the API once it's shipped. v2 can be worked on alongside v1 without
breaking any of the existing routes in deployed apps.

"""

from flask import Blueprint, jsonify, url_for

from .rest.validators import (
    get_current_lab,
)
from .samples.views import samples
from .sites.views import (
    sites,
    sitedata,
    clients,
    uploads,
    schedules,
    schedulewelltests,
    contacts,
)
from .substances.views import (
    substancegroups,
    substances,
    criterias,
    states,
)
from .users.auth import (
    auth,
    get_user,
    get_lab,
)
from .users.views import (
    users,
    consultants,
    managers,
    samplers,
    offices,
    labs,
    bplabs,
    roles,
    companies,
)
from .wells.views import (
    wells,
    wellimages,
    frequencies,
)
from .reports.views import reports
from .sites.imports.views import imports
from .sitemaps.views import (
    sitemaps,
    sitemapwells,
)
from .tests.views import (
    tests,
    testmaterials,
)

api = Blueprint('api', __name__)


@api.route('/')
def index(lab_id):
    return jsonify(
        labs_url=url_for('labs', lab_id=lab_id),
        sites_url=url_for('sites', lab_id=lab_id),
        sitedata_url=url_for('sitedata', lab_id=lab_id),
        clients_url=url_for('clients', lab_id=lab_id),
        uploads_url=url_for('uploads', lab_id=lab_id),
        schedules_url=url_for('schedules', lab_id=lab_id),
        schedulewelltests_url=url_for('schedulewelltests', lab_id=lab_id),
        contacts_url=url_for('contacts', lab_id=lab_id),
        users_url=url_for('users', lab_id=lab_id),
        user_url=url_for('user', lab_id=lab_id),
        consultants_url=url_for('consultants', lab_id=lab_id),
        companies_url=url_for('companies', lab_id=lab_id),
        managers_url=url_for('managers', lab_id=lab_id),
        samplers_url=url_for('samplers', lab_id=lab_id),
        offices_url=url_for('offices', lab_id=lab_id),
        wells_url=url_for('wells', lab_id=lab_id),
        wellimages_url=url_for('wellimages', lab_id=lab_id),
        frequencies_url=url_for('frequencies', lab_id=lab_id),
        substancegroups_url=url_for('substancegroups', lab_id=lab_id),
        substances_url=url_for('substances', lab_id=lab_id),
        criterias_url=url_for('criterias', lab_id=lab_id),
        states_url=url_for('states', lab_id=lab_id),
        samples_url=url_for('samples', lab_id=lab_id),
        tests_url=url_for('tests', lab_id=lab_id),
        testmaterials_url=url_for('testmaterials', lab_id=lab_id),
        sitemaps_url=url_for('sitemaps', lab_id=lab_id),
        sitemapwells_url=url_for('sitemapwells', lab_id=lab_id),
        reports_url=url_for('api.reports_index', lab_id=lab_id),
        auth_url=url_for('api.auth_index', lab_id=lab_id),
        roles_url=url_for('roles', lab_id=lab_id),
    )


@api.route('/auth')
def auth_index(lab_id):
    return jsonify(
        signin_url=url_for('auth.signin', lab_id=lab_id),
        signout_url=url_for('auth.signout', lab_id=lab_id),
        reset_url=url_for('auth.reset', lab_id=lab_id),
    )


@api.route('/reports')
def reports_index(lab_id):
    return jsonify(
        work_scope=url_for('reports.work_scope', lab_id=lab_id),
        sample_bottle_request_report=url_for('reports.sample_bottle_request_report', lab_id=lab_id),
        site_map=url_for('reports.site_map', lab_id=lab_id),
        notice_of_on_site_work_activity=url_for('reports.notice_of_on_site_work_activity', lab_id=lab_id),
        chain_of_custody=url_for('reports.chain_of_custody', lab_id=lab_id),
        sample_bottle_labels=url_for('reports.sample_bottle_labels', lab_id=lab_id),
        field_data_form=url_for('reports.field_data_form', lab_id=lab_id),
        cover_page=url_for('reports.cover_page', lab_id=lab_id),
        site_history=url_for('reports.site_history', lab_id=lab_id),
        field_data_results_table=url_for('reports.field_data_results_table', lab_id=lab_id),
        field_data_results_graph=url_for('reports.field_data_results_graph', lab_id=lab_id),
        groundwater_elevation_graph=url_for('reports.groundwater_elevation_graph', lab_id=lab_id),
        analytical_results_maps=url_for('reports.analytical_results_maps', lab_id=lab_id),
        analytical_results_table_n_d=url_for('reports.analytical_results_table_n_d', lab_id=lab_id),
        analytical_results_table=url_for('reports.analytical_results_table', lab_id=lab_id),
        analytical_results_graph=url_for('reports.analytical_results_graph', lab_id=lab_id),
        analytical_results_groundwater_elevation_graph=url_for('reports.analytical_results_groundwater_elevation_graph', lab_id=lab_id),
        groundwater_elevation_map=url_for('reports.groundwater_elevation_map', lab_id=lab_id),
        free_product_thickness_map=url_for('reports.free_product_thickness_map', lab_id=lab_id),
        free_product_groundwater_elevation_graph=url_for('reports.free_product_groundwater_elevation_graph', lab_id=lab_id),
        well_construction_location=url_for('reports.well_construction_location', lab_id=lab_id),
    )
