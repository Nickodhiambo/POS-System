from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models import Sum

# Time zonemodel
class MyModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    # New_Category_Model
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    # status = models.IntegerField(default=1) 
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    
# Products_model
class Products(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    image = models.ImageField(upload_to='item_image', blank=True, null=True)
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1) 
    # stock_quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code + " - " + self.name


# Sales_Records_model
class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    # date = models.DateField()
    def __str__(self):
        return self.code
    
# sales_Items_model changed sales to sale
class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)
