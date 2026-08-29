from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    num = models.IntegerField()
    sub = models.TextField()
    mes = models.TextField()

class products_desc(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=20)
    desc=models.TextField()
    daily_products=models.BooleanField(default=False)