import re
import os
import time
import math
import tempfile
import base64
import numpy as np
import matplotlib
import requests
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import scipy.interpolate

from unidecode import unidecode
from flask import make_response, send_file, request, current_app, jsonify
from functools import wraps
from PIL import Image
from matplotlib.mlab import griddata
from matplotlib.pylab import *
from numpy import *
from unidecode import unidecode
from datetime import datetime
from pprint import pprint

from sampleserve.models import Site, SiteMap
from sampleserve.config.settings import CONTOURS_PATH
from .helpers import slugify


def generateTitle(
    site_title,
    date_collected,
    date_collected_range_end,
    title_wildcard,
    substance_name,
):
    title_parts = []
    title_parts.append(site_title)
    title_parts.append(date_collected)
    title_parts.append(substance_name)
    if date_collected_range_end:
        title_parts.append(date_collected_range_end)
    if title_wildcard:
        title_parts.append(title_wildcard)
    contour_title = " - ".join(title_parts)
    return contour_title


def generateContours(
    date_collected,
    substance_name,
    well_arr,
    site_title,
    site_map,
    image,
    date_collected_range_end=False,
    title_wildcard='',
    label_over_well=False,
    crop_contours=False,
    groundwater_contours=False,
    flow_lines=False,
    site_image_alpha=1,
    status_token="",
    remove_zero_contour=True,
    logarithmic_contours=False,
    heatmap=False,
):
    # create empty arrays to fill up!
    x_values = []
    y_values = []
    z_values = []

    # iterate over wells and fill the arrays with well data
    pprint(well_arr)
    for well in well_arr:
        x_values.append(well['xpos'])
        y_values.append(well['ypos'])
        z_values.append(well['substance_sum'] if well['substance_sum'] > 0.0 else -0.01)

    # initialize numpy array as required for interpolation functions
    x = np.array(x_values, dtype=np.float)
    y = np.array(y_values, dtype=np.float)
    z = np.array(z_values, dtype=np.float)

    # create a list of x, y coordinate tuples
    points = zip(x, y)

    # create a grid on which to interpolate data
    xi, yi = np.linspace(0, image['width'], image['width']), np.linspace(0, image['height'], image['height'])
    xi, yi = np.meshgrid(xi, yi)

    # interpolate the data with the matlab griddata function (http://matplotlib.org/api/mlab_api.html# matplotlib.mlab.griddata)
    zi = griddata(x, y, z, xi, yi)

    # create a matplotlib figure and adjust the width and heights to output contours to a resolution very close to the original site_map
    fig = plt.figure(figsize=(image['width'] / 72, image['height'] / 72))

    # create a single subplot, just takes over the whole figure if only one is specified
    ax = fig.add_subplot(111, frameon=False, xticks=[], yticks=[])

    # read the database image and save to a temporary variable
    im = Image.open(image['abs_path']).convert("RGB")

    # place the site_map image on top of the figure
    ax.imshow(im, origin='upper', alpha=site_image_alpha)

    if heatmap:
        ax.imshow(zi, interpolation='bilinear', origin='upper', cmap=cmx.RdYlGn_r, alpha=0.25)

    # figure out a good linewidth
    linewidth = math.ceil(image['width'] / 1000.0)

    # create the contours (options here http://cl.ly/2X0c311V2y01)
    kwargs = {}
    if groundwater_contours:
        kwargs['colors'] = 'b'

    if heatmap:
        kwargs['colors'] = 'black'

    if logarithmic_contours:
        print "Using logarithmic contours."
        locator = matplotlib.ticker.LogLocator()
        kwargs["levels"] = np.insert(np.power(10, np.arange(0, np.floor(np.log10(z.max())))), 0, 0)
    else:
        print "Using standard contours."
        kwargs["locator"] = matplotlib.ticker.MaxNLocator(5)

    CS = plt.contour(
        xi, yi, zi,
        linewidths=linewidth,
        alpha=0.8,
        **kwargs)

    #  Check for zero contour line
    for key, value in enumerate(CS.levels):
        if value == 0:
            zero_contour = CS.collections[key]
            plt.setp(zero_contour, linewidth=linewidth * 2, color="b")

        if value == 0 and remove_zero_contour:
            CS.collections[key].remove()
            print "Contour at %G removed" % value
        else:
            print "Contour at %G" % value

    # add a streamplot
    if flow_lines:
        dy, dx = np.gradient(zi)
        plt.streamplot(xi, yi, dx, dy, color='c', density=1, arrowsize=3, arrowstyle='<-')

    # add labels to well locations
    label_kwargs = {}
    if label_over_well is True:
        label_kwargs['manual'] = points

    plt.clabel(CS,
               inline_spacing=math.floor(image['target_width'] / 100),
               fontsize=math.floor(image['target_width'] / 100),
               fmt="%G",
               **label_kwargs)

    # add scatterplot to show where well data was read
    scatter_size = math.floor(image['width'] / 20)
    plt.scatter(x, y, s=scatter_size, c='k', facecolors='none', marker=(5, 1))

    # get contour title
    contour_title = generateTitle(
        site_title=site_title,
        date_collected=date_collected,
        date_collected_range_end=date_collected_range_end,
        title_wildcard=title_wildcard,
        substance_name=substance_name,
    )

    # add descriptive title to the top of the contours
    title_font_size = math.floor(image['target_width'] / 72)
    plt.title(contour_title, fontsize=title_font_size)

    # generate a unique filename and save to a temp directory
    filename = slugify(contour_title) + str(int(time.time())) + ".pdf"
    full_path = CONTOURS_PATH + "/" + filename
    fig.set_size_inches([image['target_width'] / 72, image['target_height'] / 72])
    dir_path = os.path.dirname(os.path.realpath(__file__))
    savefig(full_path)  # bbox_inches='tight' tightens the white border

    # clears the matplotlib memory
    clf()

    # send the temporary file to the user
    path = os.path.join('/static/contours', filename)
    resp = dict(path=path, filename=filename)

    # Just return a dictionary with the path and filename
    return resp
