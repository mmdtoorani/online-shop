from django.urls import path

from customer import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('profile/', views.profile, name='profile'),
    path('orderhistory/', views.orderhistory, name='orderhistory'),
    path('cart/', views.cart, name='cart'),
    path('logout/', views.auth_logout, name='logout'),
]
