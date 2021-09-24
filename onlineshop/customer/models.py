from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from account.models import Account


class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(null=False, blank=False)
    address = models.TextField(max_length=400, null=True, blank=True)
    password = models.CharField(max_length=20, null=False)
    password2 = models.CharField(max_length=20, null=False)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.username}"


class Coupon(models.Model):
    pass


class Cart(models.Model):
    pass
