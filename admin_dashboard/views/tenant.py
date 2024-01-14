from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.shortcuts import redirect, render
from django.contrib import messages
from core.models import Tenant
from admin_dashboard.forms import TenantForm
from django.urls import reverse_lazy
from admin_dashboard.decorators import admin_login
from django.utils.decorators import method_decorator


@method_decorator(admin_login, name='dispatch')
class TenantListView(ListView):
    model = Tenant
    template_name = "tenant_list.html"
    context_object_name = "tenants"


@admin_login
def tenant_search(request):
    search_query = request.GET.get("search_query", "")
    tenant = Tenant.objects.filter(name__icontains=search_query)
    return render(
        request,
        "tenant_list.html",
        {"tenant": tenant, "search_query": search_query},
    )



@method_decorator(admin_login, name='dispatch')
class TenantDetailView(DetailView):
    model = Tenant
    template_name = "tenant_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "tenant"



@method_decorator(admin_login, name='dispatch')
class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = "tenant_form.html"
    success_url = reverse_lazy("tenant_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tenant successfully created.")
        return response



@method_decorator(admin_login, name='dispatch')
class TenantUpdateView(UpdateView):
    model = Tenant
    form_class = TenantForm
    template_name = "tenant_form.html"
    success_url = reverse_lazy("tenant_list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tenant successfully updated.")
        return response


@admin_login
def delete_tenant(request, id):
    Tenant.objects.get(id=id).delete()
    messages.success(request, "tenant deleted")
    return redirect("tenant_list")
