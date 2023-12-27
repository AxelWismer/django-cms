from django.contrib import admin
from .models import *
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Client._meta.get_fields()]
  search_fields = ['name', 'lastname']
admin.site.register(Client, ClientAdmin)