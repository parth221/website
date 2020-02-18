from django.db import models

# Create your models here.
class Product(models.Model):

    img1=models.ImageField(upload_to='product')
    price=models.IntegerField(max_length=10)
    name=models.CharField(max_length=50)

