from django.urls import path

from customer.api import views

urlpatterns = [
    path('', views.customerlist, name='customerlist'),
    path('register/', views.register, name='register'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
]
