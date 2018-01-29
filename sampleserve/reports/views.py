
import os
import httplib
import time

from pprint import pprint
from urllib import unquote
from time import sleep

from flask import Blueprint, jsonify, url_for, request, abort, json, render_template, make_response, send_file, send_from_directory

from sampleserve.models import Sample, SampleValue, Substance, SiteMapWell
from sampleserve.rest.validators import validate_schema
from sampleserve.schemas import schema, date, number, integer, add_remove, string, array, boolean
from sampleserve.models import (
    Site,
    SiteMap,
    Well,
    Criteria,
)
from sampleserve.core import db
from sampleserve.reports.helpers import slugify

from .generate_contours import generateContours
from .helpers import (
    wellSubstanceDataBySite,
    getSubstanceNames,
    loadImage,
    getBoxmapData,
    placeBoxesOnSiteMap,
    calculateBoxDimensions,
    hasLocations,
    autoPlaceBoxes,
    generate_scale_factor,
    getAnalyticalData,
)
from .create_pdf import create_pdf_from_document_url, create_pdf_from_document_content


reports = Blueprint('reports', __name__, url_prefix='/reports', template_folder='templates')


@reports.route('/work-scope', subdomain='<lab_id>')
def work_scope(lab_id):
    return jsonify(send_report="work_scope")


@reports.route('/sample-bottle-request-report', subdomain='<lab_id>')
def sample_bottle_request_report(lab_id):
    return jsonify(send_report="sample_bottle_request_report")


@reports.route('/site-map', subdomain='<lab_id>')
def site_map(lab_id):
    return jsonify(send_report="site_map")


@reports.route('/notice-of-on-site-work-activity', subdomain='<lab_id>')
def notice_of_on_site_work_activity(lab_id):
    return jsonify(send_report="notice_of_on_site_work_activity")


@reports.route('/chain-of-custody', subdomain='<lab_id>')
def chain_of_custody(lab_id):
    return jsonify(send_report="chain_of_custody")


@reports.route('/sample-bottle-labels', subdomain='<lab_id>')
def sample_bottle_labels(lab_id):
    return jsonify(send_report="sample_bottle_labels")


@reports.route('/field-data-form', subdomain='<lab_id>')
def field_data_form(lab_id):
    return jsonify(send_report="field_data_form")


@reports.route('/cover-page', subdomain='<lab_id>')
def cover_page(lab_id):
    return jsonify(send_report="cover_page")


@reports.route('/site-history', subdomain='<lab_id>')
def site_history(lab_id):
    return jsonify(send_report="site_history")


@reports.route('/field-data-results-table', subdomain='<lab_id>')
def field_data_results_table(lab_id):
    return jsonify(send_report="field_data_results_table")


@reports.route('/field-data-results-graph', subdomain='<lab_id>')
def field_data_results_graph(lab_id):
    return jsonify(send_report="field_data_results_graph")


@reports.route('/groundwater-elevation-graph', subdomain='<lab_id>')
def groundwater_elevation_graph(lab_id):
    return jsonify(send_report="groundwater_elevation_graph")


@reports.route('/analytical-results-maps', subdomain='<lab_id>')
def analytical_results_maps(lab_id):
    return jsonify(send_report="analytical_results_maps")


@reports.route('/analytical-results-table-n-d', subdomain='<lab_id>')
def analytical_results_table_n_d(lab_id):
    return jsonify(send_report="analytical_results_table_n_d")


@reports.route('/analytical-results-table', subdomain='<lab_id>')
def analytical_results_table(lab_id):
    return jsonify(send_report="analytical_results_table ")


@reports.route('/analytical-results-graph', subdomain='<lab_id>')
def analytical_results_graph(lab_id):
    return jsonify(send_report="analytical_results_graph")


@reports.route('/analytical-results-groundwater-elevation-graph', subdomain='<lab_id>')
def analytical_results_groundwater_elevation_graph(lab_id):
    return jsonify(send_report="analytical_results_groundwater_elevation_graph")


@reports.route('/groundwater-elevation-map', subdomain='<lab_id>')
def groundwater_elevation_map(lab_id):
    return jsonify(send_report="groundwater_elevation_map")


@reports.route('/free-product-thickness-map', subdomain='<lab_id>')
def free_product_thickness_map(lab_id):
    return jsonify(send_report="free_product_thickness_map")


@reports.route('/free-product-groundwater-elevation-graph', subdomain='<lab_id>')
def free_product_groundwater_elevation_graph(lab_id):
    return jsonify(send_report="free_product_groundwater_elevation_graph")


@reports.route('/well-construction-location', subdomain='<lab_id>')
def well_construction_location(lab_id):
    return jsonify(send_report="well_construction_location")


@reports.route('/get-sample-dates/<int:site_id>', methods=['GET', 'POST'], subdomain='<lab_id>')
def get_sample_dates(site_id, lab_id):
    sample_dates = Sample.query \
        .filter_by(site_id=site_id, active=True) \
        .group_by(Sample.date_collected, Sample.id) \
        .all()
    return jsonify(sample_dates=[sd.json() for sd in sample_dates])


@reports.route('/query-well-data', methods=['POST'], subdomain='<lab_id>')
def get_well_data(lab_id):
    r = request.json
    post_schema = {
        "$schema": schema,
        "properties": {
            "date_collected": date,
            "date_collected_range_end": date,
            "site_id": integer,
            "sitemap_id": integer,
            "substance_ids": array,
        },
        "required": [
            "date_collected",
            "site_id",
            "sitemap_id",
            "substance_ids"
        ]
    }
    validate_schema(r, post_schema)

    # convert to ints for the lookup function
    date_collected = r['date_collected']
    date_collected_range_end = r['date_collected_range_end'] if 'date_collected_range_end' in r else None
    site_id = r['site_id']
    site_map_id = r['sitemap_id']
    substance_ids = r['substance_ids']

    # if type(r.get('substance_ids')) is list:
    #     substance_ids = [int(substance_id) for substance_id in r.get('substance')]
    # else:
    #     substance_ids = [-1]

    # fetch the well results from the wellSubstanceDataBySite function
    well_results = wellSubstanceDataBySite(
        site_id=site_id,
        site_map_id=site_map_id,
        date_collected=date_collected,
        substance_ids=substance_ids,
        date_collected_range_end=date_collected_range_end
    )

    # return json to updateMarks ajax javascript function
    return jsonify(well_results)


@reports.route('/create-contours', methods=['POST'], subdomain='<lab_id>')
def create_contours(lab_id):
    r = request.json
    post_schema = {
        "$schema": schema,
        "type": "object",
        "properties": {
            "site_id": integer,
            "sitemap_id": integer,
            "date_collected": date,
            "substance_ids": array,
            "date_collected_range_end": date,
            "wells": {
                "type": "array",
                "items": [{
                    "type": "object",
                    "properties": {
                        "well_id": integer,
                        "xpos": number,
                        "ypos": number,
                        "substance_sum": number,
                    },
                    "required": [
                        "well_id",
                        "xpos",
                        "ypos",
                        "substance_sum",
                    ]
                }]
            },
            "title_wildcard": string,
            "label_over_well": boolean,
            "crop_contours": boolean,
            "groundwater_contours": boolean,
            "flow_lines": boolean,
            "site_image_alpha": number,
            "remove_zero_contour": boolean,
            "logarithmic_contours": boolean,
            "heatmap": boolean,
        },
        "required": [
            "site_id",
            "sitemap_id",
            "date_collected",
            "substance_ids",
            "wells",
        ]
    }
    validate_schema(r, post_schema)
    pprint(r)
    # return jsonify(dict(ok=True))
    site_map = SiteMap.query.get(r['sitemap_id'])
    site = site_map.site
    image = loadImage(site_map_id=site_map.id, url=site_map.url, target_width=site_map.width, target_height=site_map.height)
    pprint(image)

    resp = generateContours(
        date_collected=r['date_collected'],
        substance_name=getSubstanceNames(r['substance_ids']),
        well_arr=r['wells'],
        site_title=site.title,
        site_map=site_map,
        image=image,
        date_collected_range_end=r['date_collected_range_end'] if 'date_collected_range_end' in r else False,
        title_wildcard=r['title_wildcard'] if 'title_wildcard' in r else '',
        label_over_well=True if 'label_over_well' in r and r['label_over_well'] is True else False,
        crop_contours=True if 'crop_contours' in r and r['crop_contours'] is True else False,
        groundwater_contours=True if 'groundwater_contours' in r and r['groundwater_contours'] is True else False,
        flow_lines=True if 'flow_lines' in r and r['flow_lines'] is True else False,
        site_image_alpha=r['site_image_alpha'] if 'site_image_alpha' in r else 0.5,
        remove_zero_contour=True if 'remove_zero_contour' in r and r['remove_zero_contour'] is True else False,
        logarithmic_contours=True if 'contour_type' in r and r['contour_type'] == 'logarithmic' else False,
        heatmap=True if 'heatmap' in r and r['heatmap'] is True else False,
    )
    pprint(resp)
    return jsonify(resp)
    # return make_response(send_file(
    #     os.path.join('frontend/static/contours', resp['filename']), mimetype='application/pdf', as_attachment=True, attachment_filename=resp['filename']))


@reports.route('/download-analytical-boxmap', methods=['POST'], subdomain='<lab_id>')
def download_analytical_boxmap(lab_id):
    r = request.json
    # Ensure the URL was posted
    post_schema = {
        "$schema": schema,
        "type": "object",
        "properties": {
            "url": string,
        },
        "required": [
            "url",
        ]
    }
    validate_schema(r, post_schema)

    return jsonify(dict(ok=True))


@reports.route('/preview-analytical-boxmap', methods=['GET', 'POST'], subdomain='<lab_id>')
def preview_analytical_boxmap(lab_id):
    if request.method == "GET":
        # Convert these params to JSON
        r = dict(
            criteria_id=int(request.args.get('criteria_id')),
            site_id=int(request.args.get('site_id')),
            sitemap_id=int(request.args.get('sitemap_id')),
            date_collected=request.args.get('date_collected'),
            substance_ids=json.loads(request.args.get('substance_ids').replace('List ', '')),
        )
        if request.args.get('date_collected_range_end'):
            r['date_collected_range_end'] = request.args.get('date_collected_range_end')
        pprint(r)
    else:
        r = request.json

    # Validate the input
    post_schema = {
        "$schema": schema,
        "type": "object",
        "properties": {
            "criteria_id": integer,
            "site_id": integer,
            "sitemap_id": integer,
            "date_collected": date,
            "substance_ids": array,
            "date_collected_range_end": date,
        },
        "required": [
            "site_id",
            "sitemap_id",
            "date_collected",
            "substance_ids",
        ]
    }
    validate_schema(r, post_schema)

    # Validated, lets get the data needed to make the report
    date_collected = r['date_collected']
    date_collected_range_end = r['date_collected_range_end'] if 'date_collected_range_end' in r else None
    site_id = r['site_id']
    site_map_id = r['sitemap_id']
    substance_ids = r['substance_ids']
    criteria_id = r['criteria_id']

    # fetch the well results from the getBoxmapData function
    well_results = getBoxmapData(
        site_id=site_id,
        site_map_id=site_map_id,
        date_collected=date_collected,
        substance_ids=substance_ids,
        date_collected_range_end=date_collected_range_end,
        criteria_id=criteria_id,
    )

    site = Site.query.get_or_404(site_id)
    sitemap = SiteMap.query.get_or_404(site_map_id)
    substances = []
    for substance_id in substance_ids:
        substance = Substance.query.get(substance_id)
        substances.append(substance)

    # get all the data required by aj's clipping detection script
    site_map = SiteMap.query.get(site_map_id)
    box = calculateBoxDimensions(substances=substances, num_sample_dates=well_results['num_sample_dates'])
    sm_wells = SiteMapWell.query.filter_by(site_map_id=site_map_id).all()
    if criteria_id:
        criteria = Criteria.query.get(criteria_id)
    else:
        criteria = None

    # If not all the wells have xpos_fields and ypos_fields set, lets use the algo to place them automatically.
    if not hasLocations(sm_wells):
        autoPlaceBoxes(site_map=site_map, box=box, sm_wells=sm_wells)
        # We need to refresh the well_results as well
        well_results = getBoxmapData(
            site_id=site_id,
            site_map_id=site_map_id,
            date_collected=date_collected,
            substance_ids=substance_ids,
            date_collected_range_end=date_collected_range_end,
            criteria_id=criteria_id,
        )

    html = render_template(
        '/reports/analytical-boxmap.html',
        site=site,
        sitemap=sitemap,
        date_collected=date_collected,
        substance_ids=substance_ids,
        substances=substances,
        box=box,
        date_collected_range_end=date_collected_range_end,
        criteria=criteria,
        well_results=well_results)

    if request.method == "POST":
        # Return a file
        filename = slugify(site.title) + str(int(time.time())) + ".pdf"
        pdf_details = create_pdf_from_document_content(document_content=html, filename=filename)
        return jsonify(dict(path="/static/reports/" + pdf_details['filename'], filename=pdf_details['filename']))
        # return make_response(send_file(
        #     os.path.join('frontend/static/reports', pdf_details['filename']), mimetype='application/pdf', as_attachment=True, attachment_filename=filename))

    # Just return the preview
    return html


@reports.route('/preview-analytical-tables', methods=['GET', 'POST'], subdomain='<lab_id>')
def preview_analytical_tables(lab_id):
    if request.method == "GET":
        # Convert these params to JSON
        r = dict(
            criteria_id=int(request.args.get('criteria_id')),
            site_id=int(request.args.get('site_id')),
            date_collected=request.args.get('date_collected'),
            substance_ids=json.loads(request.args.get('substance_ids').replace('List ', '')),
        )
        if request.args.get('date_collected_range_end'):
            r['date_collected_range_end'] = request.args.get('date_collected_range_end')
        pprint(r)
    else:
        r = request.json

    # Validate the input
    post_schema = {
        "$schema": schema,
        "type": "object",
        "properties": {
            "criteria_id": integer,
            "site_id": integer,
            "date_collected": date,
            "substance_ids": array,
            "date_collected_range_end": date,
        },
        "required": [
            "site_id",
            "date_collected",
            "substance_ids",
        ]
    }
    validate_schema(r, post_schema)

    # Validated, lets get the data needed to make the report
    date_collected = r['date_collected']
    date_collected_range_end = r['date_collected_range_end'] if 'date_collected_range_end' in r else None
    site_id = r['site_id']
    substance_ids = r['substance_ids']
    criteria_id = r['criteria_id']

    # fetch the well results from the getBoxmapData function
    well_results = getAnalyticalData(
        site_id=site_id,
        date_collected=date_collected,
        substance_ids=substance_ids,
        date_collected_range_end=date_collected_range_end,
        criteria_id=criteria_id,
    )

    site = Site.query.get_or_404(site_id)
    substances = []
    for substance_id in substance_ids:
        substance = Substance.query.get(substance_id)
        substances.append(substance)
    if criteria_id:
        criteria = Criteria.query.get(criteria_id)
    else:
        criteria = None

    html = render_template(
        '/reports/analytical-tables.html',
        site=site,
        date_collected=date_collected,
        substance_ids=substance_ids,
        substances=substances,
        date_collected_range_end=date_collected_range_end,
        criteria=criteria,
        well_results=well_results)

    if request.method == "POST":
        # Return a file
        filename = slugify(site.title) + "-analytical-tables-" + str(int(time.time())) + ".pdf"
        pdf_details = create_pdf_from_document_content(document_content=html, filename=filename)
        return jsonify(dict(path="/static/reports/" + pdf_details['filename'], filename=pdf_details['filename']))
    # Just return the preview
    return html









