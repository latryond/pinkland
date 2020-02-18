from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    ordering = ('name', 'category', 'price')
    search_fields = ('name', 'category')
    fields=('name','category','price','discount','description','image','preview_photo')
    readonly_fields = ('preview_photo',)
