from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.db.models import ForeignKey


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

class Product(models.Model):
    name = models.CharField(max_length=50)
    functions = models.ManyToManyField(ProductFunction)
    material = models.ForeignKey(ProductMaterial, on_delete=models.CASCADE)
    categ = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.SmallIntegerField()
    thumbnail = models.ImageField(
        upload_to='assets/images/product', default='')
    discount = models.SmallIntegerField(
        default=0, help_text='unit in percentage')
    description = models.TextField(
        max_length=300, help_text='Description Maximum 300 words', blank=True)
    date_create = models.DateTimeField(db_index=True, auto_now_add=True)


class Poster(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, help_text='Description Maximum 300 words', blank=True)
    image = models.ImageField(upload_to="assets/images/poster/", default='')

