
from sampleserve.rest.views import BaseView
from .models import (
    Test,
    TestMaterial,
)


class TestView(BaseView):
    model = Test


class TestMaterialView(BaseView):
    model = TestMaterial


tests = TestView.as_view('tests')
testmaterials = TestMaterialView.as_view('testmaterials')
