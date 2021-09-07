from django.db import models

# Create your models here.

class Information(models.Model):
    Title = models.CharField(max_length=50)
    Discription = models.TextField(max_length=200)
    Orignal_price = models.IntegerField()
    Discount_price = models.IntegerField()
    Image_link = models.CharField(max_length=150)
    