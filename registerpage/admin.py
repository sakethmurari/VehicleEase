from django.contrib import admin
from .models import Register
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=('username','email','password','age','profession','phone','location','landmark')

admin.site.register(Register,RegisterAdmin)