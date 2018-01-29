
import csv
import tempfile
import requests
import pandas as pd

from numpy import nan
from pprint import pprint

from sampleserve.sites.models import Site
from sampleserve.wells.models import Well


def create_local_file_from_url(url):
    # Save file from URL
    r = requests.get(url, stream=True)
    tmp_csv = tempfile.NamedTemporaryFile(delete=False)
    with open(tmp_csv.name, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    return tmp_csv.name
