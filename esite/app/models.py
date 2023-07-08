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


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    admin_level = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validation()


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)
    product_qty = models.IntegerField(blank=True, null=True, default=1)
    product_barcode = models.IntegerField(blank=True, null=True)
    product_desc = models.TextField(default="No Description is Available")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
