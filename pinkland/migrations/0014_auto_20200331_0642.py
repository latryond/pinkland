# Generated by Django 3.0.3 on 2020-03-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkland', '0013_auto_20200331_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default='/media/low-poly-texture-80.png', upload_to='product_image/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_image'),
        ),
    ]
