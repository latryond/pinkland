from django.contrib import admin
from .models import Product, ProductImages, Poster, ProductMaterial, ProductCategory, ProductFunction
import logging

class ProductImageInline(admin.TabularInline):
    model = ProductImages
    fields = ['image', ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'categ', 'price',)
    ordering = ('name', 'categ', 'price')
    search_fields = ('name', 'categ')
    fields = (('discount','is_discount'),'name','functions','material','categ','price','thumbnail','description',)
    inlines = [ProductImageInline, ]


class PosterAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductFunctionAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductFunction, ProductFunctionAdmin)
admin.site.register(Poster, PosterAdmin)
