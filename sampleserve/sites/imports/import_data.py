# -*- coding: utf-8 -*-

import csv
import tempfile
import requests
import pandas as pd
from flask import abort, g, jsonify
import sys

from numpy import nan
from pprint import pprint
from dateutil import parser

from sampleserve.core import db
from sampleserve.models import (
    Sample,
    SampleValue,
    Schedule,
    Substance,
    Company,
    Well,
    Site,
    Client,
    Upload,
)

from ..helpers import create_local_file_from_url
from sampleserve.rest.errors import BadUpload


def isNaN(num):
    return num != num


def normalizeSubstanceValue(in_unit, out_unit, value):
    # Change values
    try:
        if value == "yes":
            value = 1.00
        elif value == "no":
            value = 0.00
        else:
            value = float(value.replace('<', '').replace(',', '').replace(' ', ''))
    except:
        print(value, type(value))
        raise BadUpload("Value <%s> must be a number." % value)

    # Normalize units
    if in_unit and not isNaN(in_unit):
        in_unit = in_unit.lower()
    if out_unit:
        out_unit = out_unit.lower()

    # Run unit conversions
    if any([
            in_unit == out_unit,
            in_unit == "-",
            isNaN(in_unit)
        ]):
        return value * 1.00
    elif (in_unit == "ppb" or in_unit == "ppb (ug/l)") and out_unit == "ppm":
        return value * 0.001
    elif (in_unit == "ppb" and out_unit == "ppb (ug/l)"):
        return value
    elif in_unit == "ppt" and out_unit == "ppb":
        return value * 0.001
    elif in_unit == "ppt" and out_unit == "ppm":
        return value * 0.000001
    elif (in_unit == "ppm" or in_unit == "ppm (mg/l)") and out_unit == "mg/l":
        return value * 1.00
    elif (in_unit == "us/cm" or in_unit == "µs/cm") and out_unit == "ms/cm":
        return value * 1000.00
    elif in_unit == "feet" and out_unit == "ft":
        return value
    elif (in_unit == "in" or in_unit == "inches") and out_unit == "ft":
        return value / 12.00
    elif in_unit == "c" or in_unit == "celcius":
        return value * 1.00
    else:
        raise BadUpload("%s => %s converstion not supported for value %s" % (in_unit, out_unit, value))


def maxValue(unit):
    # Set the value to the maximum value for free product
    if unit == "ppt":
        return 10000000000
    if unit == "ppb":
        return 1000000000
    if unit == "ppm":
        return 100000000
    else:
        return -1


def import_data(upload_type, company_id, lab_id, site_id=None, url=None, local_csv=None, dry_run=False):
    # Pull down the CSV file from a remote URL if its not local
    if not local_csv:
        local_csv = create_local_file_from_url(url)
    # Read the data from the uploaded CSV
    import_info = pd.read_csv(local_csv, names=None, nrows=3, usecols=[0], header=None, skipinitialspace=False).to_dict()
    df = pd.read_csv(local_csv, names=None, header=4, index_col=0, mangle_dupe_cols=True)  # Not using .to_dict('index') anymore because it destroys multiple wells
    data = df.reset_index().to_dict('index')
    pprint(data)

    title = import_info[0][0]
    client_name = import_info[0][1]
    site_name = import_info[0][2]
    cas_info = data[0]
    unit_info = data[1]
    # return dict(import_info=import_info, cas_info=cas_info, unit_info=unit_info, data=data)
    # print("title: %s" % title)
    # print("site_name: %s" % site_name)

    # Clear the session from previous dry_runs
    db.session.remove()

    # Filter the upload for major things
    if not client_name:
        raise BadUpload("Client name not found. Client name should be in the 1st column, 2nd row.")
    if not site_name:
        raise BadUpload("Site name not found. Site name should be in the 1st column, 3nd row.")
    if 'Sample ID' not in unit_info:
        raise BadUpload("Sample ID column not found.")
    if unit_info['Sample ID'] != 'Unit':
        raise BadUpload("Unit row not found in data, check the example upload.")
    if cas_info['Sample ID'] != 'CAS':
        raise BadUpload("CAS row not found in data, check the example upload.")
    if len(data) < 3:
        raise BadUpload("Not enough columns in data.")

    # Make sure the lab does not have any other unsent uploads, because uploading multiple and then sending will cause errors
    pending_uploads = Upload.query.filter_by(company_id=company_id, sent=False, lab_upload=True).count()
    if pending_uploads:
        raise BadUpload('You can only have one unsent upload at a time. Please send or delete unsent upload.')

    # Look up data and prep for import
    company = Company.query.get(company_id)  # Always set
    if site_id:
        # User is uploading to a particular site
        site = Site.query.get(site_id)
        client = Client.query.filter_by(company_id=company_id, name=client_name).first()  # Find a client that matches client_name
        if not client:
            raise BadUpload('\"%s\" client name does not match \"%s.\"' % (client_name, site.client.name))
        if site.title != site_name:
            raise BadUpload('\"%s\" site title does not match \"%s.\"' % (site_name, site.title))
    else:
        # The lab is uploading
        lab_upload = True
        # Look up client or create
        client = Client.query.filter_by(company_id=company_id, name=client_name).first()  # Find a client that matches client_name
        if not client:
            client = Client(company_id=company_id, name=client_name)
            db.session.add(client)
        # Look up site or create
        site = client.sites.filter_by(company_id=company_id, title=site_name, lab_id=lab_id).first()
        if not site:
            site = Site(company_id=company_id, client_id=client.id, title=site_name, lab_id=lab_id)
            db.session.add(site)

    # Now lets look up the active substance
    cas_numbers = cas_info
    cas_numbers.pop('Sample ID', None)
    cas_numbers.pop('Date Collected', None)

    substances = dict()
    for substance_name, cas in cas_numbers.iteritems():
        if isNaN(cas):
            raise BadUpload("Missing CAS number for %s" % substance_name)
        cas = cas.replace('-', '').replace(' ', '').upper()
        substance = Substance.query.filter_by(cas_sanitized=cas, active=True).first()
        if not substance:
            raise BadUpload("Substance not found for CAS # %s" % cas)
        if upload_type == "field_data" and not substance.field_data:
            raise BadUpload("%s is not allowed in field data." % substance.title)
        if upload_type == "lab_data" and substance.field_data:
            raise BadUpload("%s is not allowed in lab data." % substance.title)
        substances[substance_name] = substance
    # pprint(substances)

    units = unit_info
    cas_numbers.pop('Sample ID', None)
    units.pop('Date Collected', None)

    # Remove the CAS and Unit from the data so all we have are wells
    data.pop(0)
    data.pop(1)

    # Data remaining is a list of wells
    imported_wells = []

    # Get the number of wells the site currently has
    # If the well_count is greater than 0, we won't allow an upload to create a new well
    # This is to avoid creating a well due to a typo and because well ids should be case sensitive
    well_count = Well.query.filter_by(site_id=site.id).count()
    sample_dates = []
    sample_ids = []

    # For each well in the upload
    for key, well_row in data.iteritems():
        # Look up the well
        well_title = well_row['Sample ID']
        well = Well.query.filter_by(site_id=site.id, title=well_title).first()

        if not well and not well_count:
            # Well not found, lets create it, but for sites with no existing wells
            well = Well(site_id=site.id, title=well_title, notes="Automatically created from Lab Data Upload")
            db.session.add(well)
        elif well:
            # Matching well found
            pass
        else:
            raise BadUpload("Existing wells found on this site and none matched: %s" % well_title)

        imported_wells.append(well)

        # Create the sample
        collection_date = parser.parse(well_row['Date Collected']).date()
        sample = Sample.query.filter_by(site_id=site.id, date_collected=collection_date).first()
        if not sample:
            sample = Sample(site_id=site.id, date_collected=collection_date)
            db.session.add(sample)
        if sample.date_collected not in sample_dates:
            sample_dates.append(sample.date_collected)
        if sample.id not in sample_ids:
            sample_ids.append(sample.id)

        # Create a schedule with a matching date
        schedule = Schedule.query.filter_by(site_id=site.id, date=collection_date).first()
        if not schedule:
            schedule = Schedule(site_id=site.id, date=collection_date)
            db.session.add(schedule)

        # Remove Date Collected from the well_row so only substances are left
        well_row.pop('Sample ID')
        well_row.pop('Date Collected')

        for substance_name, substance_value in well_row.iteritems():
            # Iterate over substances per well, create samples and sample_values
            # print("substance_name", substance_name)
            # print("substance_value", substance_value)
            # Record the substance_value if it's not blank or --
            if not isNaN(substance_value) and substance_value != "--":
                # Find sample value entry
                sample_value = SampleValue.query.filter_by(
                    substance_id=substances[substance_name].id,
                    sample_id=sample.id,
                    well_id=well.id
                ).first()
                if not sample_value:
                    # Doesn't exist, create it
                    sample_value = SampleValue(
                        substance_id=substances[substance_name].id,
                        sample_id=sample.id,
                        well_id=well.id)
                # If it contains <, set the value to zero, but save the original value in less_than
                if '<' in substance_value:
                    sample_value.less_than = normalizeSubstanceValue(
                        in_unit=units[substance_name],
                        out_unit=substances[substance_name].unit,
                        value=substance_value)
                    sample_value.value = 0.00
                elif substance_name == 'Free product (yes/no)':
                    if substance_value.lower() in ['1', 'yes', 'true']:
                        sample_value.free_product = True
                    elif substance_value.lower() in ['0', 'no', 'false']:
                        sample_value.free_product = False
                    else:
                        raise BadUpload("\"%s\" is not a valid value for Free Product. Use Yes or No." % substance_value)
                elif substance_value == 'FP':
                    sample_value.free_product = True
                    sample_value.value = maxValue(unit=units[substance_name])
                elif substance_value == 'ND':
                    sample_value.non_detect = True
                else:
                    sample_value.value = normalizeSubstanceValue(
                        in_unit=units[substance_name],
                        out_unit=substances[substance_name].unit,
                        value=substance_value)
                db.session.add(sample_value)

    # Commit the data permanently if all checks pass!
    if not dry_run:
        db.session.commit()
    else:
        db.session.remove()

    res = dict(
        site_name=site_name,
        site_id=site.id,
        client_name=client.name,
        sample_dates=sample_dates,
        sample_ids=sample_ids,
        imported_wells_count=len(imported_wells))
    pprint(res)

    return res
