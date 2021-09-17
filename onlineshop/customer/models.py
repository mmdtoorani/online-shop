from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Coupon(models.Model):
    pass


class Cart(models.Model):
    pass
