from django import forms
from core.models import Tenant


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = "__all__"



