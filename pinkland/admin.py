from django.contrib import admin
from .models import Product, ProductImage, Poster

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ['image',]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    ordering = ('name', 'category', 'price')
    search_fields = ('name', 'category')
    inlines = [ProductImageInline,]

class PosterAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    
# class CompanyAdmin(admin.ModelAdmin):

        
admin.site.register(Product, ProductAdmin)
admin.site.register(Poster, PosterAdmin)
# admin.site.register(Company, CompanyAdmin)
# admin.site.register(ProductImage, ProductImageInline)
