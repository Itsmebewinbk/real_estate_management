from django.views.generic import (
    ListView,
)
from common.models import Country, State


class CountryListView(ListView):
    model = Country
    template_name = "countries_list.html"
    context_object_name = "countries"


class StateListView(ListView):
    model = State
    template_name = "states_list.html"
    context_object_name = "states"
