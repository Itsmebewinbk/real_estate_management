from rest_framework import generics
from moonhive_real_estate.permission import IsAuthenticatedUser, IsAdmin
from core.models import Unit, Property
from api.v1.core.serializers import UnitSerializer, PropertySerializer
from rest_framework.filters import SearchFilter


class UnitListCreateView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    filter_backends = (SearchFilter,)
    search_fields = [
        "name",
    ]


class UnitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    allowed_methods = ("GET", "PATCH", "DELETE")


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    filter_backends = (SearchFilter,)
    search_fields = ("name",)


class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    allowed_methods = ("GET", "PATCH", "DELETE")
