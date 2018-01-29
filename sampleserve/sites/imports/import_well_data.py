
import csv
import tempfile
import requests
import pandas as pd

from numpy import nan
from pprint import pprint

from sampleserve.models import (
    Well,
    Client,
    Site,
)
from sampleserve.rest.errors import BadUpload

from ..helpers import create_local_file_from_url
from .import_data import isNaN


def import_well_data(site_id, upload_type=None, url=None, local_csv=None):
    if not local_csv:
        local_csv = create_local_file_from_url(url)
    names = [
        "Well/Sample ID",
        "Top of Casing Elevation",
        "Well Diameter (inches)",
        "Well Material",
        "Screen Length (ft)",
        "Sampling Technique",
        "GPS Latitude (decimal)",
        "GPS Longitude (decimal)",
        "Estimated Depth to Water (ft)",
        "Measured Depth to Bottom (ft)",
        "Well Sampling Purge Water Disposal",
        "Well Notes",
    ]
    import_info = pd.read_csv(local_csv, names=None, nrows=3, usecols=[0], header=None, skipinitialspace=False).to_dict()
    data = pd.read_csv(local_csv, names=None, header=4, index_col=0).to_dict('index')

    title = import_info[0][0]
    client_name = import_info[0][1]
    site_name = import_info[0][2]
    # print("Upload title: %s" % title)
    # print("Site name: %s" % site_name)

    # Map the fields to the model
    mapping = {
        "Well/Sample ID": "title",
        "Top of Casing Elevation": "top_of_casing",
        "Well Diameter (inches)": "diameter",
        "Well Material": "material",
        "Screen Length (ft)": "screenlength",
        "Sampling Technique": "sampletechnique",
        "GPS Latitude (decimal)": "latitude",
        "GPS Longitude (decimal)": "longitude",
        "Estimated Depth to Water (ft)": "est_depth_to_water",
        "Measured Depth to Bottom (ft)": "depth_to_bottom",
        "Well Sampling Purge Water Disposal": "purge_water_disposal",
        "Well Notes or other Well Specific Information": "notes"
    }

    # Allowed values
    allowed_values = dict(
        sampletechnique=["Low Flow", "Grab Sample", "Other"],
        material=["Other", "PVC", "Steel"],
        purge_water_disposal=["Pour on ground", "Place in container", "Other"],
        title="Well Information")
    # Update existing wells, add new ones.
    site = Site.query.get_or_404(site_id)
    if not site:
        raise BadUpload('Site not found!')
    if site_name != site.title:
        raise BadUpload('\"%s\" site title does not match \"%s.\"' % (site_name, site.title))
    client = Client.query.filter_by(name=client_name).first()  # Find a client that matches client_name
    if not client:
        raise BadUpload('\"%s\" client name does not match \"%s.\"' % (client_name, site.client.name))

    for well_id in data:
        # print("Updating well_id: " + well_id)
        # Check to see if there is an existing well to update
        well = site.wells.filter_by(title=well_id).first()
        if not well:
            well = Well(title=well_id, site_id=site_id)
        for k, v in data[well_id].iteritems():
            # Validate the field
            # Sanitize the key in the header
            key = k.replace('\xca', ' ')
            if mapping[key] in allowed_values:
                # Shorten the input / support some legacy values
                if type(v) is str and v.lower() == "pour on ground near well":
                    v = "Pour on ground"
                if type(v) is str and v.lower() == "place in container on site":
                    v = "Place in container"
                if type(v) is str and v.lower() == "3 volumes/grab":
                    v = "Grab Sample"
                # Check to make sure the value is allowed
                if v not in allowed_values[mapping[key]]:
                    raise BadUpload('%s is not an allowed value for %s' % (v, key))
            # Set the value on the well model
            setattr(well, mapping[key], v)
        well.save_or_error()
