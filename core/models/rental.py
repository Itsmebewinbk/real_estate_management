from django.db import models


class Rental(models.Model):
    property = models.ForeignKey(
        "core.Property",
        on_delete=models.CASCADE,
        related_name="rentals",
    )
    unit = models.ForeignKey(
        "core.Unit",
        on_delete=models.SET_NULL,
        related_name="rentals",
        null=True,
        blank=True,
    )
    tenant = models.ForeignKey(
        "core.Tenant",
        on_delete=models.SET_NULL,
        related_name="rentals",
        null=True,
        blank=True,
    )

    rent_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    deposit_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
