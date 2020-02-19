from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ['image',]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    ordering = ('name', 'category', 'price')
    search_fields = ('name', 'category')
    inlines = [ProductImageInline,]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
