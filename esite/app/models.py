from django.db import models
import re

# Create your models here.


class Validation(models.Manager):
    def reg_validation(self, data):
        error = {}
        # First Name Validation:
        if len(data['first_name']) < 3:
            error['short_first_name'] = "First Name Must Have at Least 3 Characters"
        
        # Last Name Validation:
        if len(data['last_name']) < 3:
            error['short_last_name'] = "Last Name Must Have at Least 3 Characters"
        
        all_emails = User.objects.all()
        # Email Validation : Already Exists
        for email in all_emails:
            if email.email == data['email']:
                error['email_exist'] = "This email address already used!"
        # Email Validation : Regression
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']):
            error['email_reg'] = "Invalid email address!"
        
        # Password Confirmation Validation :  Password and Password Confirmation must be the same
        if data['password'] != data['password_confirmation']:
            error['password_confirmation'] = "Password and Password Confirmation should Match!"
        # Password Validation : Password must be at least 8 characters
        if len(data['password']) < 8 :
            error['password'] = "Password Must be at least 8 characters"
        # Password Validation : Password Regex
        PASSWORD_REGEX = re.compile(r'^.*(?=.{8,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9!@#$%^&*()_+={}?:~\[\]]+$')
        if not PASSWORD_REGEX.match(data['password']):
            error['password_regex'] = "Password must have 'Lower Case' / 'Upper Case' / 'Number' / 'Symbol (@ # $ % ^ & + = _ -)'"
        return error
    
    def cat_validation(self,data):
        error = {}
        if len(data['cat_name']) <= 0 :
            error['cat_name'] = "Please Enter a Name for the Category"
        return error

    def product_validation(self,data,image):
        error = {}
        if len(data['product_name']) <= 0:
            error['product_name'] = "Please Enter a Name for the Product"
        if not('product_image' in image) :
            error['no_image']="Please Upload an Image for the Product"
        if data['product_category'] == 'Please Select a Category':
            error['Please Select a Category'] = "Please Select a Category"
        return error



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    admin_level = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validation()


class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # product_category
    objects = Validation()

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_qty = models.IntegerField(blank=True, null=True, default=1)
    product_barcode = models.IntegerField(blank=True, null=True)
    product_desc = models.TextField(default="No Description is Available")
    product_image = models.ImageField(null=True, blank=True,upload_to='images')
    categories = models.ForeignKey(Category,related_name='product_category', on_delete=models.CASCADE, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =Validation()

# class Category(models.Model):
#     cat_name = models.CharField(max_length=255)
#     products = models.ForeignKey(Product,related_name='product_category', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
