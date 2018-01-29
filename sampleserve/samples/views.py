
from sampleserve.rest.views import BaseView
from .models import Sample


class SamplesView(BaseView):
    model = Sample

samples = SamplesView.as_view('samples')
