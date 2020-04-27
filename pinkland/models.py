from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.db.models import ForeignKey
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField( upload_to="assets/images/" )
    aboutus = models.CharField(max_length=1000)
    phone = models.CharField(max_length=10)


class ProductMaterial(models.Model):
    name = models.CharField(max_length=50);
    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class ProductFunction(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class ProductImages(models.Model):
    p_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="assets/images/product/")

def validate_discount(value):
    if value in range(100):
        return value
    else:
        raise ValidationError("This value should within 0 to 99 ")

class Product(models.Model):
    name = models.CharField(verbose_name='產品名稱',max_length=50)
    functions = models.ManyToManyField(ProductFunction,verbose_name='功能')
    material = models.ForeignKey(ProductMaterial, on_delete=models.CASCADE,verbose_name='材料')
    categ = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,verbose_name='分類')
    price = models.SmallIntegerField(verbose_name='價錢',)
    thumbnail = models.ImageField(
        verbose_name='縮圖',upload_to='assets/images/product', default='')
    is_discount = models.BooleanField(verbose_name='啟用 ?',default=False)
    discount = models.SmallIntegerField(verbose_name='折扣',default=0, help_text='unit in percentage',validators=[validate_discount])
    description = models.TextField(
        verbose_name='描述',max_length=300, help_text='Description Maximum 300 words', blank=True)
    date_create = models.DateTimeField(db_index=True, auto_now_add=True)

    def get_thumbnail_display(self):
        return(self.thumbnail.url)

class Poster(models.Model):
    title = models.CharField(verbose_name='標題',max_length=50)
    description = models.TextField(verbose_name='描述',max_length=300, help_text='Description Maximum 300 words', blank=True)
    image = models.ImageField(verbose_name='圖片',upload_to="assets/images/poster/", default='')
