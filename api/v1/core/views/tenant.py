from rest_framework import generics
from moonhive_real_estate.permission import IsAuthenticatedUser, IsAdmin
from core.models import Tenant
from api.v1.core.serializers import TenantSerializer
from rest_framework.filters import SearchFilter


class TenantListCreateView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    filter_backends = (SearchFilter,)
    search_fields = ("name",)


class TenantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    allowed_methods = ("GET", "PATCH", "DELETE")

