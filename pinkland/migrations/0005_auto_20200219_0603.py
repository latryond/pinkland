# Generated by Django 3.0.3 on 2020-02-19 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinkland', '0004_auto_20200211_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Description Maximum 300 words', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('rose_quartz', '粉水晶'), ('amethyst', '紫水晶'), ('citrine', '黃水晶'), ('super_seven', '超級七'), ('gold_rutilated_quartz', '金髮晶'), ('green_phantom', '綠幽靈'), ('moon_stone', '月亮石'), ('labradorite', '拉長石'), ('tigers_eye', '虎眼石'), ('clear_quartz', '白水晶'), ('Aquamarine', '海藍寶'), ('pcink_beryl', '摩根石'), ('rhodochrosite', '紅紋石'), ('strawberry_quartz', '草莓石'), ('white_phantom', '白幽靈'), ('sunstone', '太陽石'), ('agate', '瑪瑙')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinkland.Product')),
            ],
        ),
    ]