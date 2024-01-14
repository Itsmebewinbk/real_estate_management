from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.shortcuts import redirect, render
from django.contrib import messages
from core.models import Property, Unit
from admin_dashboard.forms import PropertyForm, UnitForm
from django.urls import reverse_lazy
from admin_dashboard.decorators import admin_login
from django.utils.decorators import method_decorator

@method_decorator(admin_login, name='dispatch')
class PropertyListView(ListView):
    model = Property
    template_name = "property_list.html"
    context_object_name = "properties"


@method_decorator(admin_login, name='dispatch')
class PropertyDetailView(DetailView):
    model = Property
    template_name = "property_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "property"


@method_decorator(admin_login, name='dispatch')
class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = "property_add.html"
    success_url = reverse_lazy("property_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Property was successfully created.")
        return response

@admin_login
def property_search(request):
    search_query = request.GET.get("search_query", "")
    properties = Property.objects.filter(name__icontains=search_query)
    return render(
        request,
        "property_list.html",
        {"properties": properties, "search_query": search_query},
    )


@method_decorator(admin_login, name='dispatch')
class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "property_edit.html"
    success_url = reverse_lazy("property_list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Property was successfully updated.")
        return response

@admin_login
def delete_property(request, id):
    Property.objects.get(id=id).delete()
    messages.success(request, "Property deleted")
    return redirect("property_list")


# Unit views

@method_decorator(admin_login, name='dispatch')
class UnitListView(ListView):
    model = Unit
    template_name = "unit_list.html"
    form = UnitForm
    context_object_name = "units"

@admin_login
def unit_search(request):
    search_query = request.GET.get("search_query", "")
    units = Unit.objects.filter(name__icontains=search_query)
    return render(
        request,
        "unit_list.html",
        {"units": units, "search_query": search_query},
    )


@method_decorator(admin_login, name='dispatch')
class UnitDetailView(DetailView):
    model = Unit
    template_name = "unit_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "unit"


@method_decorator(admin_login, name='dispatch')
class UnitCreateView(CreateView):
    model = Unit
    form_class = UnitForm
    template_name = "unit_form.html"
    success_url = reverse_lazy("unit_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Unit was successfully created.")
        return response


@method_decorator(admin_login, name='dispatch')
class UnitUpdateView(UpdateView):
    model = Unit
    form_class = UnitForm
    template_name = "unit_form.html"
    success_url = reverse_lazy("unit_list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Unit was successfully created.")
        return response

@admin_login
def delete_unit(request, id):
    Unit.objects.get(id=id).delete()
    messages.success(request, "Unit deleted")
    return redirect("unit_list")
