from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    admin_level = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)
    product_qty = models.IntegerField(blank=True , null=True, default=1)
    product_barcode = models.IntegerField(blank=True , null=True)
    product_desc = models.TextField(default="No Description is Available")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

