from django import forms
from core.models import Property, Unit


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = (
            "name",
            "property",
            "cost",
            "type",
            "image",
            "is_active",
        )
