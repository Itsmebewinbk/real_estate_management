from django.db import models


UNIT_TYPES = [
    ("1BHK", "1BHK"),
    ("2BHK", "2BHK"),
    ("3BHK", "3BHK"),
    ("4BHK", "4BHK"),
]


class Property(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)

    features = models.TextField()
    phone_code = models.ForeignKey(
        "common.Country", on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    state = models.ForeignKey(
        "common.State",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    zipcode = models.CharField(
        max_length=10,
    )
    address = models.CharField(
        max_length=250,
    )

    mobile = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )


class Unit(models.Model):
    name = models.CharField(max_length=255)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="units"
    )
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=4, choices=UNIT_TYPES)
    tenant = models.ForeignKey("Tenant", on_delete=models.SET_NULL, null=True)
    image = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_occupied = models.BooleanField(default=False)
