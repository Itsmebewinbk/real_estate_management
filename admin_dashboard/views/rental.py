from django.views.generic import (
    ListView,
    CreateView,
)
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from core.models import Rental, Unit
from admin_dashboard.forms import RentalForm
from django.urls import reverse_lazy
from admin_dashboard.decorators import admin_login
from django.utils.decorators import method_decorator


@method_decorator(admin_login, name='dispatch')
class RentalListView(ListView):
    model = Rental
    template_name = "rental_list.html"
    context_object_name = "rentals"


@method_decorator(admin_login, name='dispatch')
class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = "rental_form.html"
    success_url = reverse_lazy("rental_list")

    def form_valid(self, form):
        unit_id = self.kwargs.get("id")
        unit = get_object_or_404(Unit, id=unit_id)
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")
        existing_rentals = Rental.objects.filter(
            start_date__lte=end_date, end_date__gte=start_date, unit=unit
        )

        if existing_rentals.exists():
            messages.error(
                self.request,
                "unit is already booked on this date",
            )
            return self.form_invalid(form)
        if start_date and end_date and start_date >= end_date:
            messages.error(
                self.request,
                "Start date must be before end date.",
            )
            return self.form_invalid(form)
        form.instance.property = unit.property
        form.instance.unit = unit
        form.instance.unit.tenant = form.instance.tenant
        form.instance.unit.is_occupied = True
        form.instance.unit.save(update_fields=["tenant", "is_occupied"])
        form.instance.rent_amount = unit.cost
        response = super().form_valid(form)
        messages.success(self.request, "Rental successfully created.")
        return response

@admin_login
def delete_rental(request, id):
    Rental.objects.get(id=id).delete()
    messages.success(request, "Rental deleted")
    return redirect("rental_list")
