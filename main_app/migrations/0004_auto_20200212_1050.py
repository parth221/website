# Generated by Django 3.0.3 on 2020-02-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200212_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_h',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_w',
        ),
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(upload_to='product'),
        ),
    ]
