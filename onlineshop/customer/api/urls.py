from django.urls import path

from customer.api import views

urlpatterns = [
    path('', views.customerlist, name='customerlist'),
    path('<int:pk>', views.customerdetail, name='customerdetail'),
    path('register/', views.register, name='register'),
]
