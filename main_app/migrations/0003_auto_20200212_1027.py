# Generated by Django 3.0.3 on 2020-02-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200212_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(height_field='image_h', upload_to='product', width_field='image_w'),
        ),
    ]
