from django.urls import path
from api.v1.core.views import (
    # unit
    UnitListCreateView,
    UnitRetrieveUpdateDestroyView,
    # property
    PropertyListCreateView,
    PropertyRetrieveUpdateDestroyView,
    # tenant
    TenantListCreateView,
    TenantRetrieveUpdateDestroyView,
    # rental
    RentalListCreateView,
    RentalRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        "properties/",
        PropertyListCreateView.as_view(),
    ),
    path(
        "property/<int:pk>/",
        PropertyRetrieveUpdateDestroyView.as_view(),
    ),
    path("units/", UnitListCreateView.as_view(), name="unit-list"),
    path(
        "unit/<int:pk>/",
        UnitRetrieveUpdateDestroyView.as_view(),
        name="unit-detail",
    ),
    path("tenants/", TenantListCreateView.as_view(), name="tenant-list"),
    path(
        "tenant/<int:pk>/",
        TenantRetrieveUpdateDestroyView.as_view(),
        name="tenant-detail",
    ),
    path("unit/<unit_id>/rentals/", RentalListCreateView.as_view(), name="rental-list"),
    path(
        "rental/<int:pk>/",
        RentalRetrieveUpdateDestroyView.as_view(),
        name="rental-detail",
    ),
]
