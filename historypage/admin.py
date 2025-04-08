from django.contrib import admin
from .models import BookingHistory
# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('email','type','car_name','car_number','actual_price','price','days')
admin.site.register(BookingHistory,HistoryAdmin)