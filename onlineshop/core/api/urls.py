from django.urls import path, include


urlpatterns = [
    path('customers/', include('customer.api.urls')),
    path('orders/', include('order.api.urls')),
    path('products/', include('product.api.urls')),
]