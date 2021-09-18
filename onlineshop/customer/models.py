from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if not email or not first_name or not last_name:
            raise ValueError('The information must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.get_full_name()
        user.save()
        return user


class User(AbstractUser):
    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Coupon(models.Model):
    pass


class Cart(models.Model):
    pass
