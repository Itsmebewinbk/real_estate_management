from django.contrib import admin
from core.models import Property,Unit,Tenant,Rental

admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Rental)
