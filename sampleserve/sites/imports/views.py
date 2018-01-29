
from pprint import pprint

from flask import Blueprint, jsonify, url_for, request, abort, json, render_template, make_response, send_file, send_from_directory

from sampleserve.sites.imports.import_data import import_data


imports = Blueprint('imports', __name__, url_prefix='/imports', template_folder='templates')


@imports.route('/test-lab-data-upload', subdomain='<lab_id>')
def test_lab_data_upload(lab_id):
    resp = import_data(
        upload_type='lab_data',
        company_id=53,
        lab_id=0,
        site_id=129,
        url="https://cdn.filestackcontent.com/9syXBSaSuGP1VTvlQbJT",
        local_csv=None,
        dry_run=True)
    pprint(resp)
    return jsonify(resp)


@imports.route('/test-field-data-upload', subdomain='<lab_id>')
def test_field_data_upload(lab_id):
    resp = import_data(
        upload_type='field_data',
        company_id=53,
        lab_id=0,
        site_id=129,
        url="https://cdn.filestackcontent.com/qEMXHWX3SlWBTaxKUGn4",
        local_csv=None,
        dry_run=True)
    pprint(resp)
    return jsonify(resp)
