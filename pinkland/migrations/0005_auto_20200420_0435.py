# Generated by Django 3.0.5 on 2020-04-20 04:35

from django.db import migrations, models
import pinkland.models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkland', '0004_auto_20200420_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(default=0, help_text='unit in percentage', validators=[pinkland.models.validate_discount], verbose_name='折扣'),
        ),
    ]
