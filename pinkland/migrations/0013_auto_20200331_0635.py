# Generated by Django 3.0.3 on 2020-03-31 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkland', '0012_auto_20200323_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default='/media/low-poly-texture-80.png', upload_to='media'),
        ),
    ]
