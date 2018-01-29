
import httplib

from flask import abort, g, jsonify, request
from flask_login import (
    login_required,
    current_user,
)

from sampleserve.rest.validators import validate_schema
from sampleserve.rest.views import (
    BaseView,
    PrivateView,
)
from sampleserve.rest.validators import (
    validate_json,
)
from sampleserve.rest.errors import IntegrityError, handle_unauthorized

from sampleserve.models import (
    Site,
    SiteData,
    Client,
    Upload,
    Schedule,
    ScheduleWellTests,
    Contact,
    State,
)
from sampleserve.sites.forms import (
    SiteDataForm,
)
from sampleserve.emails.emails import send_lab_results_async
from sampleserve.sites.imports.import_data import import_data
from sampleserve.sites.imports.import_well_data import import_well_data
from sampleserve.core import db

from . import schemas
from pprint import pprint


def validateStateId(g):
    if 'state_id' not in g.body:
        raise IntegrityError('state_id is required.')
    elif type(g.body['state_id']) is not int:
        raise IntegrityError('Bad value for state_id.')
    else:
        state = State.query.filter_by(id=g.body['state_id']).first()
        if not state:
            raise IntegrityError('Invalid state_id.')


class SitesView(BaseView):
    model = Site

    def post(self):
        validate_schema(g.body, schemas.post_site)

        site = self.model()
        site.patch(g.body)

        if 'state_id' in g.body:
            state = State.query.get(g.body['state_id'])
            site.state = state.title

        # Client is required
        client = Client.query.filter_by(id=g.body['client_id']).first()
        if not client:
            raise IntegrityError(dict(client="Client not found"))
        site.company_id = client.company_id
        site.lab_id = g.current_lab.id

        site.save_or_error()
        res = site.json()

        return jsonify(res)

    def patch(self, id):
        validate_schema(g.body, schemas.patch_site)

        site = self.model.query.get(id)
        site.patch(g.body)

        if 'state_id' in g.body:
            state = State.query.get(g.body['state_id'])
            site.state = state.title

        site.save_or_error()
        res = site.json()
        return jsonify(res)


class SiteDataView(BaseView):
    model = SiteData

    def post(self):
        r = request.json
        site = self.model()
        form = SiteDataForm.from_json(r)
        if form.validate():
            form.validate(site)
            site.save_or_error()
            res = site.json()
            return jsonify(res)
        else:
            raise IntegrityError(form.errors)

    def patch(self, id):
        r = request.json
        site = self.model.query.get(id)
        form = SiteDataForm.from_json(r)
        if form.validate():
            form.populate_obj(site)
            site.save_or_error()
            res = site.json()
            return jsonify(res)
        else:
            raise IntegrityError(form.errors)


class ScheduleView(PrivateView):
    model = Schedule

    def post(self):
        if g.current_role in schemas.schedule:
            validate_schema(g.body, schemas.schedule[g.current_role])

        schedule = self.model()
        schedule.patch(g.body)

        if 'copy_params' in g.body and g.body['copy_params']:
            # Copy tests and other info from old schedule
            print(g.body['copy_params'])
            copy_schedule = Schedule.query.filter_by(date=g.body['copy_params']).first()
            if copy_schedule:
                print(copy_schedule)
                schedule.timeofday = copy_schedule.timeofday
                schedule.starttime = copy_schedule.starttime
                schedule.endtime = copy_schedule.endtime
                schedule.typeofactivity = copy_schedule.typeofactivity
                schedule.release_number = copy_schedule.release_number
                schedule.frequency_association = copy_schedule.frequency_association
                schedule.test_ids = copy_schedule.test_ids
                schedule.tests = copy_schedule.tests
                schedule.schedule_well_tests = copy_schedule.schedule_well_tests
                schedule.gauged_wells = copy_schedule.gauged_wells
                schedule.skipped_wells = copy_schedule.skipped_wells

        schedule.save_or_error()

        res = schedule.json()
        return jsonify(res)

    def patch(self, id):
        if g.current_role not in ['Admin', 'Anonymous'] and current_user.id == id:
            g.current_role = 'Own'

        if g.current_role in schemas.schedule:
            validate_schema(g.body, schemas.schedule[g.current_role])

        schedule = self.model.query.get(id)
        schedule.patch(g.body)
        schedule.save_or_error()

        res = schedule.json()
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

        # Get past foreign key errors by removing from relationship tables
        instance.tests = []
        instance.schedule_well_tests = []
        instance.gauged_wells = []
        instance.skipped_wells = []
        instance.save_or_error()
        instance.delete_or_error()
        return ('', httplib.NO_CONTENT)


class ScheduleWellTestsView(BaseView):
    model = ScheduleWellTests


class ClientsView(BaseView):
    model = Client

    def post(self):
        # Do some pre-processing of the upload
        if 'name' not in g.body or not g.body['name'].strip():
            raise IntegrityError("Name required for creating new clients.")

        client = self.model()
        client.patch(g.body)
        client.save_or_error()

        res = client.json()
        return jsonify(res)


class UploadView(PrivateView):
    model = Upload

    def post(self):
        # Do some pre-processing of the upload
        if 'upload_type' in g.body and 'url' in g.body:
            # types: well_data, field_data, lab_data
            if g.body['upload_type'] == 'well_data':
                import_well_data(upload_type='well_data', site_id=g.body['site_id'], url=g.body['url'])
            if g.body['upload_type'] == 'field_data':
                import_data(lab_id=g.current_lab.id, upload_type='field_data', company_id=g.body['company_id'], site_id=g.body['site_id'], url=g.body['url'])
            if g.body['upload_type'] == 'lab_data':
                if 'dry_run' in g.body and g.body['dry_run'] == 'true':
                    # Process the upload but don't save yet
                    print("Processing but not saving data!")
                    success = import_data(lab_id=g.current_lab.id, upload_type='lab_data', company_id=g.body['company_id'], url=g.body['url'], dry_run=True)
                else:
                    import_data(lab_id=g.current_lab.id, upload_type='lab_data', company_id=g.body['company_id'], url=g.body['url'], site_id=g.body['site_id'])

        upload = self.model()
        upload.patch(g.body)
        upload.save_or_error()

        res = upload.json()
        return jsonify(res)

    def patch(self, id):
        upload = self.model.query.get(id)

        if 'sent' in g.body:
            print("sent in g.body!")
            # Send email notification
            send_lab_results_async(upload)

        upload.patch(g.body)
        upload.save_or_error()
        res = upload.json()
        return jsonify(res)


class ContactView(PrivateView):
    model = Contact

sites = SitesView.as_view('sites')
sitedata = SiteDataView.as_view('sitedata')
clients = ClientsView.as_view('clients')
uploads = UploadView.as_view('uploads')
schedules = ScheduleView.as_view('schedules')
schedulewelltests = ScheduleWellTestsView.as_view('schedulewelltests')
contacts = ContactView.as_view('contacts')
