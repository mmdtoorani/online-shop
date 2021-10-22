from django.urls import path

from product.api import views

urlpatterns = [
    path('', views.ProductAPIView.as_view()),
    path('<str:category>/', views.ProductAPIView.as_view()),
    # path('<int:pk>/', views.ProductByPkAPIView.as_view()),
    path('categories/', views.CategoryAPIView.as_view())

]
