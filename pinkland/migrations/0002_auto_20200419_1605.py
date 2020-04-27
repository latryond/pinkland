# Generated by Django 3.0.5 on 2020-04-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkland', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(default=0, help_text='unit in percentage'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=False),
        ),
    ]