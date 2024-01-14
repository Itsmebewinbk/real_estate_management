from rest_framework import serializers
from core.models import Unit, Property


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        exclude = ("tenant", "is_occupied")


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
