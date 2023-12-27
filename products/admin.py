from django.contrib import admin

# Register your models here.
# products_app/admin.py
from django.contrib import admin
from .models import Product, ProductCategory, Service

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Service)