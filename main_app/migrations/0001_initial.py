# Generated by Django 3.0.3 on 2020-02-12 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='media')),
                ('price', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]