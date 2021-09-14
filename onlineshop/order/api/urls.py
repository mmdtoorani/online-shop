from django.urls import path

from order.api import views

urlpatterns = [
    path('', views.orderlist, name='orderlist'),
    path('<int:pk>', views.orderdetail, name='orderdetail'),

]
