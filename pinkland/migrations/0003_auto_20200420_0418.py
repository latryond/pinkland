# Generated by Django 3.0.5 on 2020-04-20 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkland', '0002_auto_20200419_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=False, verbose_name='discounting ?'),
        ),
    ]
