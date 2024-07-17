from django.db import models

# Create your models here!
class users(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

class products(models.Model):
    Productname=models.CharField(max_length=50)
    Companyname=models.CharField(max_length=50)
    Price=models.IntegerField()
    Image=models.ImageField(upload_to='static/images')