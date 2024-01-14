from rest_framework.generics import ListAPIView
from common.models import State, Country


from api.v1.common.serializers import (
    CountryListSerializer,
    StateListSerializer,
)

from rest_framework.filters import SearchFilter

from api.v1.common.filters import CountryFilterBackend


class CountriesListView(ListAPIView):
    serializer_class = CountryListSerializer
    filter_backends = [
        SearchFilter,
    ]
    search_fields = ["name", "code"]


class StateListView(ListAPIView):
    serializer_class = StateListSerializer
    filter_backends = [SearchFilter, CountryFilterBackend]
    search_fields = ["name", "code", "country__name"]
