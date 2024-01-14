from coreapi import Field
from rest_framework.filters import BaseFilterBackend


class CountryFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            Field(
                name="country", location="query", required=False, type="string"
            ),
        ]

    def filter_queryset(self, request, queryset, view):
        country = request.query_params.get("country", None)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset