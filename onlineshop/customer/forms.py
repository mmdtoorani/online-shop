from django import forms
from django.contrib.auth import authenticate

from customer.models import Customer


class SignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', 'password2', ]
        many = False
