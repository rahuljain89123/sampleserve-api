
from sampleserve.rest.views import BaseView
from .models import (
    SubstanceGroup,
    Substance,
    Criteria,
    State,
)


class SubstanceGroupsView(BaseView):
    model = SubstanceGroup


class SubstancesView(BaseView):
    model = Substance


class CriteriasView(BaseView):
    model = Criteria


class StatesView(BaseView):
    model = State

substancegroups = SubstanceGroupsView.as_view('substancegroups')
substances = SubstancesView.as_view('substances')
criterias = CriteriasView.as_view('criterias')
states = StatesView.as_view('states')
