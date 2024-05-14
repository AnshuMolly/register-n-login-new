from django.contrib import admin
from home.models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_username','service_password',)

admin.site.register(Service,ServiceAdmin)