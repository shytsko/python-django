from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
