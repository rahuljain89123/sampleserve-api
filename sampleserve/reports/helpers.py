
import os
import re
import json
import jsonschema
import hashlib
import requests
import math
import random

from unidecode import unidecode
from pprint import pprint
from datetime import datetime
from PIL import Image
from collections import namedtuple

from flask import Blueprint, g, jsonify, session, current_app
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators, TextAreaField, SelectField, SelectMultipleField, HiddenField, RadioField, BooleanField, FileField, DateField, IntegerField, FormField
from wtforms.validators import DataRequired, ValidationError, Required, Optional, Length, URL, Email, NumberRange

from sampleserve.models import Sample, SampleValue, Well, Substance, SiteMapWell, Criteria, CriteriaValues
from sampleserve.core import db


def sorted_nicely(list):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list, key=alphanum_key)


def wellSubstanceDataBySite(site_id, site_map_id, date_collected, substance_ids, date_collected_range_end=None):
    # Get all the wells
    wells = Well.query.filter_by(site_id=site_id).all()
    my_wells = {}
    for w in wells:
        my_well = {
            'id': w.id,
            'xpos_fields': w.xpos_fields,
            'xpos': w.xpos,
            'title': w.title,
            'site_id': w.site_id,
            'ypos': w.ypos,
            'ypos_fields': w.ypos_fields,
            'top_of_casing': w.top_of_casing,
            'est_depth_to_water': w.est_depth_to_water,
            'substances': None,
            'substance_sum': None
        }
        my_wells[w.id] = my_well

    if date_collected_range_end:
        # query a date range
        samples = Sample.query \
            .filter_by(site_id=site_id, active=True) \
            .filter(Sample.date_collected >= date_collected) \
            .filter(Sample.date_collected <= date_collected_range_end) \
            .all()
    else:
        samples = Sample.query \
            .filter_by(site_id=site_id, active=True) \
            .filter(Sample.date_collected == date_collected) \
            .all()
    if not samples:
        return dict(my_wells={})

    well_ids = []
    for s in samples:
        values = s.values.filter(SampleValue.substance_id.in_(substance_ids)).all()
        for v in values:
            if v.well_id not in well_ids:
                well_ids.append(v.well_id)

        # Overwrite well with one that has substances and substance_sum
        for well_id in well_ids:
            sm_well = SiteMapWell.query.filter_by(site_map_id=site_map_id, well_id=well_id).first()
            if not sm_well:
                my_wells[well_id] = {
                    'substances': {},
                    'substance_sum': 0
                }
            else:
                my_wells[sm_well.well.id] = {
                    'id': sm_well.well.id,
                    'xpos_fields': sm_well.xpos_fields,
                    'xpos': sm_well.xpos,
                    'title': sm_well.well.title,
                    'site_id': sm_well.site_id,
                    'ypos': sm_well.ypos,
                    'ypos_fields': sm_well.ypos_fields,
                    'top_of_casing': sm_well.well.top_of_casing,
                    'est_depth_to_water': sm_well.well.est_depth_to_water,
                    'substances': {},
                    'substance_sum': 0
                }

        for v in values:
            my_wells[v.well_id]['substances'][v.substance_id] = {
                'substance_id': v.substance_id,
                'substance_name': v.substance.title,
                'substance_value': v.value,
            }
            my_wells[v.well_id]['substance_sum'] += v.value
    return dict(my_wells=my_wells)


def getBoxmapData(site_id, site_map_id, date_collected, substance_ids, date_collected_range_end=None, criteria_id=None):
    # Get all the wells
    my_wells = {}
    sm_wells = SiteMapWell.query.filter_by(site_map_id=site_map_id).all()

    if date_collected_range_end:
        # query a date range
        samples = Sample.query \
            .filter_by(site_id=site_id, active=True) \
            .filter(Sample.date_collected >= date_collected) \
            .filter(Sample.date_collected <= date_collected_range_end) \
            .all()
    else:
        samples = Sample.query \
            .filter_by(site_id=site_id, active=True) \
            .filter(Sample.date_collected == date_collected) \
            .all()

    # No samples found, return an empty dictionary
    if not samples:
        return dict(my_wells={}, num_sample_dates=0)

    for sm_well in sm_wells:
        my_wells[sm_well.well.id] = sm_well.__dict__
        my_wells[sm_well.well.id].pop('_sa_instance_state', None)
        my_wells[sm_well.well.id]['samples'] = []

    for sample in samples:
        for well_id in my_wells:
            my_sample = {}
            my_sample['date_collected'] = sample.date_collected
            my_sample['substances'] = {}
            for substance_id in substance_ids:
                # Add substance values
                well_substance_values = sample.values.filter_by(substance_id=substance_id, well_id=well_id).first()
                if well_substance_values:
                    my_sample['substances'][substance_id] = well_substance_values.__dict__
                    my_sample['substances'][substance_id].pop('_sa_instance_state', None)
                    my_sample['substances'][substance_id]['criteria_values'] = None
                    # Add criteria values
                    criteria_values = CriteriaValues.query.filter_by(criteria_id=criteria_id, substance_id=substance_id).first()
                    if criteria_values:
                        my_sample['substances'][substance_id]['criteria_values'] = criteria_values.__dict__
                        # pprint(my_sample['substances'][substance_id]['criteria_values'])
                        # my_sample['substances'][substance_id]['criteria_values'].pop('_sa_instance_state', None)

            # Add this sample to the list
            my_wells[well_id]['samples'].append(my_sample)

    return dict(my_wells=my_wells, num_sample_dates=len(samples))


def getAnalyticalData(site_id, date_collected, substance_ids, date_collected_range_end=None, criteria_id=None):
    # Get all the wells
    my_wells = {}
    wells = Well.query.filter_by(site_id=site_id).all()

    if date_collected_range_end:
        # query a date range
        samples = Sample.query \
            .filter_by(site_id=site_id, active=True) \
            .filter(Sample.date_collected >= date_collected) \
            .filter(Sample.date_collected <= date_collected_range_end) \
            .all()
    else:
        samples = Sample.query \
            .filter_by(site_id=site_id, active=True) \
            .filter(Sample.date_collected == date_collected) \
            .all()

    # No samples found, return an empty dictionary
    if not samples:
        return dict(my_wells={}, num_sample_dates=0)

    well_titles = []
    for well in wells:
        well_titles.append(well.title)
    sorted_well_titles = sorted_nicely(set(well_titles))
    pprint(sorted_well_titles)

    for well in wells:
        my_wells[well.title] = well.__dict__
        my_wells[well.title].pop('_sa_instance_state', None)
        my_wells[well.title]['samples'] = []

    for sample in samples:
        for well_title in my_wells:
            my_sample = {}
            my_sample['date_collected'] = sample.date_collected
            my_sample['substances'] = {}
            for substance_id in substance_ids:
                # Add substance values
                well_substance_values = sample.values.filter_by(substance_id=substance_id, well_id=my_wells[well_title]['id']).first()
                if well_substance_values:
                    my_sample['substances'][substance_id] = well_substance_values.__dict__
                    my_sample['substances'][substance_id].pop('_sa_instance_state', None)
                    my_sample['substances'][substance_id]['criteria_values'] = None
                    # Add criteria values
                    criteria_values = CriteriaValues.query.filter_by(criteria_id=criteria_id, substance_id=substance_id).first()
                    if criteria_values:
                        my_sample['substances'][substance_id]['criteria_values'] = criteria_values.__dict__
                        # pprint(my_sample['substances'][substance_id]['criteria_values'])
                        # my_sample['substances'][substance_id]['criteria_values'].pop('_sa_instance_state', None)

            # Add this sample to the list
            my_wells[well_title]['samples'].append(my_sample)

    return dict(my_wells=my_wells, num_sample_dates=len(samples), sorted_well_titles=sorted_well_titles)



_punct_re = re.compile(r'[\t !"# $%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return unicode(delim.join(result))


def parseDate(stringythingy):
    datetime_obj = datetime.strptime(str(stringythingy), '%Y%m%d')
    return datetime_obj.strftime('%Y-%m-%d')


def generateSafeFilename(site_map_id):
    # Generate a filename that no one can guess
    key = "mBhGVX(6HCnfpy"
    new_filename = "%s_site_map_id_%s" % (key, site_map_id)
    h = hashlib.new('ripemd160')
    h.update(new_filename)
    filename = h.hexdigest() + ".jpg"
    return filename


def downloadFile(url, abs_path):
    r = requests.get(url, stream=True)
    with open(abs_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return abs_path


def loadImage(site_map_id, url, target_width=None, target_height=None):
    # Load paths
    path = current_app.config['SITEMAPS_PATH']
    filename = generateSafeFilename(site_map_id)

    # Set the path to save the file locally
    abs_path = os.path.join(path, filename)

    try:
        # Try to open this file
        with open(abs_path, 'rb'):
            # File exists
            print("file exists")
            pass
    except IOError:
        print("file does not exist")
        # File does not exist, lets download it from the url and save locally
        downloadFile(url=url, abs_path=abs_path)

    # Open the image with PIL and get the width and height
    im = Image.open(abs_path)
    width, height = im.size
    image = {
        #  'stream': imageBase64,
        'filename': filename,
        'abs_path': abs_path,
        'height': height,
        'width': width,
        'target_width': target_width,
        'target_height': target_height
    }
    return image


def getSitemapInfo(site_map_id):

    key = "mBhGVX(6HCnfpy"
    new_filename = "%s_site_map_id_%s" % (key, site_map_id)
    h = hashlib.new('ripemd160')
    h.update(new_filename)
    filename = h.hexdigest() + ".jpg"
    public_url_base = "https://s3.us-east-2.amazonaws.com/sampleserve/public/"
    public_url = public_url_base + filename
    print(public_url)
    return dict(public_url=public_url, filename=filename)


def getSubstanceNames(substance_ids):
    substance_names = ''
    for substance_id in substance_ids:
        substance = Substance.query.get(substance_id)
        substance_names = substance_names + " " + substance.title
    return substance_names


def generate_border_size():
    # Comment out the below line when we want to actually
    # have a border
    return {'width': 0, 'height': 0}

    # return a border size that gives us enough room for at least 2X the boxes
    count = 1
    site_map_area = (site_map.height + (box['height'] * count * 2)) * (site_map.width + (box['width'] * count * 2))
    minimum_area = 2 * wells_count * box['height'] * box['width']
    while site_map_area < minimum_area:
        site_map_area = (site_map.height + (box['height'] * count * 2)) * (site_map.width + (box['width'] * count * 2))
        count += 1
    return {'width': box['width'] * count, 'height': box['height'] * count}


def generate_scale_factor(site_map, box, wells_count):
    site_map_area = site_map.height * site_map.width
    minimum_area = 3 * wells_count * box['height'] * box['width']
    if site_map_area > minimum_area:
        return 1
    optimal_scale = minimum_area / float(site_map_area)
    if optimal_scale > 3:
        # Lets do a max scaling of 3 so the boxes don't get too small when printed.
        return 3
    return optimal_scale


LocationGenerator = namedtuple('LocationGenerator', "x_begin steps y_begin tries_start tries_end")
opts = [
    LocationGenerator(x_begin=-1, steps=20, y_begin=-1, tries_start=0, tries_end=400),
    LocationGenerator(x_begin=-2, steps=40, y_begin=-2, tries_start=400, tries_end=760),
    LocationGenerator(x_begin=-2, steps=10, y_begin=-1, tries_start=760, tries_end=960),
    LocationGenerator(x_begin=-2, steps=40, y_begin=1, tries_start=960, tries_end=1320),
    LocationGenerator(x_begin=1, steps=10, y_begin=-1, tries_start=1320, tries_end=1520),
    LocationGenerator(x_begin=-3, steps=60, y_begin=-3, tries_start=1520, tries_end=2120),
    LocationGenerator(x_begin=-3, steps=60, y_begin=2, tries_start=2120, tries_end=2720),

    LocationGenerator(x_begin=-3, steps=10, y_begin=-2, tries_start=2720, tries_end=3120),
    LocationGenerator(x_begin=2, steps=10, y_begin=-2, tries_start=3120, tries_end=3520),
]
step_size = 0.1


def generate_location(current_location, sm_well, scale_factor, box, tries, site_map):
    i = 0

    # This is an attempt to generalize the logic below, using the LocationGenerator
    if tries >= opts[-1].tries_end:
        return {'xpos': round(random.random() * (site_map.width * scale_factor)), 'ypos': round(random.random() * (site_map.height * scale_factor))}

    else:
        # Test comment
        while i < len(opts) and tries >= opts[i].tries_end:
            i += 1

        loc_gen = opts[i]
        x_factor = (tries % loc_gen.steps) * 0.1 + loc_gen.x_begin
        xpos = sm_well.xpos * scale_factor + (x_factor * box['width'])

        y_factor = math.floor((tries - loc_gen.tries_start) / loc_gen.steps) * 0.1 + loc_gen.y_begin
        ypos = sm_well.ypos * scale_factor + (y_factor * box['height'])
        if x_factor > -0.01 and x_factor < 0.01:
            xpos += 30
        if x_factor > -1.01 and x_factor < -0.99:
            xpos -= 30

        return {'xpos': xpos, 'ypos': ypos}


def isBoxValid(loc, site_map, scale_factor, box_size):
    return (
        loc['xpos'] >= 0 and loc['xpos'] <= (site_map.width * scale_factor - box_size['width']) and
        loc['ypos'] >= 0 and loc['ypos'] <= (site_map.height * scale_factor - box_size['height']))


def doesBoxOverlap(loc, sm_wells, box_locations, box, scale_factor):
    # Check if location is valid
    for sm_well in sm_wells:
        # x coordinate is between left and right of box
        sm_well_x = sm_well.xpos * scale_factor
        sm_well_y = sm_well.ypos * scale_factor
        if (sm_well_x > loc['xpos'] and sm_well_x < loc['xpos'] + box['width'] and
            # y coordinate is between bottom and top of box
            sm_well_y > loc['ypos'] and sm_well_y < loc['ypos'] + box['height']):
            return True

    for m_well_id, box_location in box_locations.iteritems():
        if (box_location['xpos'] > loc['xpos'] - box['width'] and box_location['xpos'] < loc['xpos'] + box['width'] and
            box_location['ypos'] > loc['ypos'] - box['height'] and box_location['ypos'] < loc['ypos'] + box['height']):
            return True


Line = namedtuple("Line", 'p1 p2')
Point = namedtuple("Point", 'x y')


def generate_line(box, sm_well, scale_factor):
    return {'a': {'x': box['xpos'], 'y': box['ypos'] + 20}, 'b': {'x': sm_well.xpos * scale_factor, 'y': sm_well.ypos * scale_factor}}


def doesLineCross(cur_line, lines):
    for line in lines:
        if doesIntersect(cur_line, line):
            return True
    return False


def doesIntersect(line1, line2):

    return (ccw(line1['a'], line2['a'], line2['b']) != ccw(line1['b'], line2['a'], line2['b']) and
            ccw(line1['a'], line1['b'], line2['a']) != ccw(line1['a'], line1['b'], line2['b']))


def ccw(a, b, c):
    return (c['y'] - a['y']) * (b['x'] - a['x']) > (b['y'] - a['y']) * (c['x'] - a['x'])


def placeBoxesOnSiteMap(site_map, box, sm_wells):
    # pprint('SITEMAP WELLS FOR placeBoxesOnSiteMap')
    # pprint(sm_wells)
    # border = generate_border_size(site_map, box, len(sm_wells))
    scale_factor = generate_scale_factor(site_map, box, len(sm_wells))
    box_locations = {}
    lines = []
    for sm_well in sm_wells:
        loc = None
        tries = 0
        loc_found = False
        cur_line = None

        while not loc_found:
            loc = generate_location(current_location=loc, sm_well=sm_well, scale_factor=scale_factor, box=box, tries=tries, site_map=site_map)
            cur_line = generate_line(box=loc, sm_well=sm_well, scale_factor=scale_factor)

            # Generate new location
            tries += 1

            if tries >= 7500:
                loc_found = True
                continue
            # check if new location is valid
            if not isBoxValid(loc=loc, site_map=site_map, scale_factor=scale_factor, box_size=box):
                continue

            # check if new location overlaps with any locations already marked out on the map
            if doesBoxOverlap(loc=loc, sm_wells=sm_wells, box_locations=box_locations, box=box, scale_factor=scale_factor):
                continue

            if doesLineCross(cur_line=cur_line, lines=lines):
                continue

            loc_found = True

        box_locations[sm_well.well.id] = loc
        lines.append(cur_line)

    return {'boxes': box_locations, 'scale_factor': scale_factor, 'border': generate_border_size()}


def calculateBoxDimensions(substances, num_sample_dates):
    # Calculate height
    height = 40 + (len(substances) * 22)

    # Calculate width
    max_substance_char_length = 0
    for substance in substances:
        if len(substance.title) > max_substance_char_length:
            max_substance_char_length = len(substance.title)
    width = (max_substance_char_length * 10) + (90 * num_sample_dates)

    # Lets add a 10px padding so there is some breathing room between boxes
    height = height + 10
    width = width + 10

    # Set some minimum widths
    if height < 150:
        height = 150
    if width < 220:
        width = 220

    return dict(height=height, width=width)


def hasLocations(sm_wells):
    # Make sure all xpos_fields and ypos_fields are set on every sm_well
    for sm_well in sm_wells:
        if not sm_well.xpos_fields or not sm_well.ypos_fields:
            return False
    return True


def autoPlaceBoxes(site_map, box, sm_wells):
    locations = placeBoxesOnSiteMap(site_map=site_map, box=box, sm_wells=sm_wells)
    for sm_well in sm_wells:
        sm_well.xpos_fields = locations['boxes'][sm_well.well.id]['xpos']
        sm_well.ypos_fields = locations['boxes'][sm_well.well.id]['ypos']
    scale_factor = generate_scale_factor(site_map, box, len(sm_wells))
    site_map.scale = scale_factor
    db.session.commit()
    return sm_wells

