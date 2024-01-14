from rest_framework import serializers
from core.models import Rental, Unit
from django.shortcuts import get_object_or_404


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        exclude = ("property", "unit")

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        start_date = validated_data.get("start_date")
        end_date = validated_data.get("end_date")
        self.unit = get_object_or_404(Unit, id=self.context.get("unit_id"))
        validated_data["unit"] = self.unit
        existing_rentals = Rental.objects.filter(
            start_date__lte=end_date, end_date__gte=start_date, unit=self.unit
        )
        if existing_rentals.exists():
            raise serializers.ValidationError(
                "unit is already booked on this date",
            )
        if start_date and end_date and start_date >= end_date:
            raise serializers.ValidationError(
                "Start date must be before end date.",
            )

        return validated_data

    def create(self, validated_data):
        unit = get_object_or_404(Unit, id=self.context.get("unit_id"))
        validated_data["unit"] = unit
        validated_data["property"] = unit.property
        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["unit_name"] = instance.unit.name
        data["property_name"] = instance.property.name
        return data
