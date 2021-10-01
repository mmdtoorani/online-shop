from django.urls import path

from product.api import views

urlpatterns = [
    path('', views.ProductViewSet.as_view({'get': 'productlist'}), name='productlist'),
    path('categories/', views.CategoryViewSet.as_view({'get': 'category_list'}), name='category_list'),
    path('category<int:pk>/', views.ProductViewSet.as_view({'get': 'category'}), name='category'),

]
