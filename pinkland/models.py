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
        ('pink_beryl','摩根石'),
        ('rhodochrosite','紅紋石'),
        ('strawberry_quartz','草莓石'),    
        ('white_phantom','白幽靈'),
        ('sunstone','太陽石'),
        ('agate','瑪瑙'),
    )
    body_part_choice = (
        ('bracelet', '手鏈'),
        ('pendant', '吊墜'),
        ('ring', '戒指'),
        ('earring', '耳環'),
        ('furnishing', '擺設'),
        ('necklace', '項鏈')
    )
    body_part_choice = (
        ('bracelet', '手鏈'),
        ('pendant', '吊墜'),
        ('ring', '戒指'),
        ('earring', '耳環'),
        ('furnishing', '擺設'),
        ('necklace', '項鏈')
    )
    func_choice = (
        ('carrer','事業'),
        ('relationship','人緣'),
        ('health','健康'),
        ('emotion','情緒'),
        ('stress_relieve','減壓'),
        ('love','愛情'),
        ('purification', '淨化'),
        ('wealth','財運'),
        ('exorcise_evil', '辟邪'),
        ('away_from_snob', '防小人')
    )
    list_display = ('name', 'category','body_part')
    name = models.CharField(max_length=30)
    thumbnail = models.ImageField(
        upload_to='../media/', default='/media/low-poly-texture-80.png')
    category = models.CharField(max_length=100, choices=category_choice)
    body_part = models.CharField(max_length=100, choices=body_part_choice, default='bracelet')
    func = models.CharField(max_length=100, choices=func_choice,blank=True)
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
