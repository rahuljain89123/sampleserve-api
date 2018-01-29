
from sampleserve.rest.views import BaseView
from .models import (
    SiteMap,
    SiteMapWell,
)


class SiteMapView(BaseView):
    model = SiteMap


class SiteMapWellsView(BaseView):
    model = SiteMapWell

sitemaps = SiteMapView.as_view('sitemaps')
sitemapwells = SiteMapWellsView.as_view('sitemapwells')
