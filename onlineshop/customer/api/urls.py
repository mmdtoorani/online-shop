from django.urls import path

from customer.api import views

urlpatterns = [
    path('', views.customerlist, name='customerlist'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
]
