from django import forms
from core.models import Rental


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = (
            "tenant",
            "deposit_amount",
            "is_active",
            "start_date",
            "end_date",
        )
