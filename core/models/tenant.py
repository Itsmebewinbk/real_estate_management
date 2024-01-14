from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    document_proofs = models.URLField()
    phone_code = models.ForeignKey(
        "common.Country",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    mobile = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    state = models.ForeignKey(
        "common.State",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    zipcode = models.CharField(
        max_length=10,
        
    )
    address = models.CharField(
        max_length=250,
       
    )

