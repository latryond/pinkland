from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

class Product(models.Model):
    category_choice=(
        ('rose_quartz','粉水晶'),
        ('amethyst','紫水晶'),
        ('citrine','黃水晶'),
        ('super_seven','超級七'),
        ('gold_rutilated_quartz','金髮晶'),
        ('green_phantom','綠幽靈'),
        ('moon_stone','月亮石'),
        ('labradorite','拉長石'),
        ('tigers_eye','虎眼石'),
        ('clear_quartz','白水晶'),
        ('Aquamarine','海藍寶'),
        ('pcink_beryl','摩根石'),
        ('rhodochrosite','紅紋石'),
        ('strawberry_quartz','草莓石'),    
        ('white_phantom','白幽靈'),
        ('sunstone','太陽石'),
        ('agate','瑪瑙'),
    )
    list_display = ('name', 'category' )
    name = models.CharField( max_length = 30 )
    category = models.CharField( max_length = 100,choices=category_choice )
    price = models.DecimalField( max_digits=7, decimal_places=2 )
    discount = models.IntegerField(default=0)
    description = models.TextField( max_length=300, help_text='Description Maximum 300 words', blank=True)
    ProductImages = None
    is_sale = False
    
    def preview_photo(self):
        return mark_safe('<img src="{}" style="width:50%" />'.format(self.image.url))
    preview_photo.short_description = 'Image'
    preview_photo.allow_tags = True

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product_id = models.ForeignKey('Product',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', blank=True)
