from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getfilename(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time, filename)
    return os.path.join('uploads/', new_filename)

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getfilename)
    description =  models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Show, 1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=getfilename)
    quantity =  models.IntegerField(null=False, blank=False)
    original_price =  models.FloatField(null=False, blank=False)
    selling_price =  models.FloatField(null=False, blank=False)
    description =  models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Show, 1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-Default, 1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty * self.product.selling_price

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
