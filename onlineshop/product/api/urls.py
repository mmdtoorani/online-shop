from django.urls import path

from product.api import views

urlpatterns = [
    path('', views.productlist, name='productlist'),
    path('<int:pk>', views.productdetail, name='productdetail'),

]
