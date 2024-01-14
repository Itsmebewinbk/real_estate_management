from rest_framework import serializers
from common.models import State, Country


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"
