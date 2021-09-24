from django import forms
from phonenumber_field.formfields import PhoneNumberField

from customer.models import Customer


class SignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', 'password2', ]
        many = False

    # password = forms.CharField(label='password')
    # password2 = forms.CharField(label='password2')
        # phone = PhoneNumberField(label='phone')
#
#
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['first_name', 'last_name', ]
#     password = forms.CharField(label='password')


