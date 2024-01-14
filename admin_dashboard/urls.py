from django.urls import path
from admin_dashboard.views import (
    # auth
    login_view,
    logout_view,
    # property
    PropertyCreateView,
    delete_property,
    property_search,
    PropertyDetailView,
    PropertyUpdateView,
    PropertyListView,
    # unit
    UnitListView,
    UnitCreateView,
    UnitDetailView,
    UnitUpdateView,
    delete_unit,
    unit_search,
    # tenant
    TenantListView,
    TenantCreateView,
    TenantDetailView,
    TenantUpdateView,
    delete_tenant,
    tenant_search,
    # rental
    RentalCreateView,
    RentalListView,
    delete_rental,
    # common
    CountryListView,
    StateListView,
)

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "property/create/",
        PropertyCreateView.as_view(),
        name="property_create",
    ),
    path(
        "property/",
        PropertyListView.as_view(),
        name="property_list",
    ),
    path(
        "property/update/<int:id>/",
        PropertyUpdateView.as_view(),
        name="property_edit",
    ),
    path(
        "property/detail/<int:id>/",
        PropertyDetailView.as_view(),
        name="property_detail",
    ),
    path(
        "property/delete/<int:id>/",
        delete_property,
        name="property_delete",
    ),
    path(
        "unit/create/",
        UnitCreateView.as_view(),
        name="unit_create",
    ),
    path(
        "unit/",
        UnitListView.as_view(),
        name="unit_list",
    ),
    path(
        "unit/update/<int:id>/",
        UnitUpdateView.as_view(),
        name="unit_edit",
    ),
    path(
        "unit/detail/<int:id>/",
        UnitDetailView.as_view(),
        name="unit_detail",
    ),
    path(
        "unit/delete/<int:id>/",
        delete_unit,
        name="unit_delete",
    ),
    # tenant
    path(
        "tenant/create/",
        TenantCreateView.as_view(),
        name="tenant_create",
    ),
    path(
        "tenant/",
        TenantListView.as_view(),
        name="tenant_list",
    ),
    path(
        "tenant/update/<int:id>/",
        TenantUpdateView.as_view(),
        name="tenant_edit",
    ),
    path(
        "tenant/detail/<int:id>/",
        TenantDetailView.as_view(),
        name="tenant_detail",
    ),
    path(
        "tenant/delete/<int:id>/",
        delete_tenant,
        name="tenant_delete",
    ),
    # rentals
    path(
        "unit/detail/<int:id>/renant/create/",
        RentalCreateView.as_view(),
        name="rental_create",
    ),
    path(
        "rental/",
        RentalListView.as_view(),
        name="rental_list",
    ),
    path(
        "rental/delete/<int:id>/",
        delete_rental,
        name="rental_delete",
    ),
    path(
        "countries/",
        CountryListView.as_view(),
        name="country_list",
    ),
    path(
        "states/",
        StateListView.as_view(),
        name="state_list",
    ),
    path("property/search/", property_search, name="property_search"),
    path("tenant/search/", tenant_search, name="tenant_search"),
    path("unit/search/", unit_search, name="unit_search"),
]
