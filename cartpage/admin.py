from django.contrib import admin
from .models import vehicle
# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    # list_filter=('name',)
    # search_fields=('name',)
    list_display=('name','vehicle_type','car_number','book')

admin.site.register(vehicle,VehicleAdmin)