from django.contrib import admin

from app.models import Category, Manufacturer, Product

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)
