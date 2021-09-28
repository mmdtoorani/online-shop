from django.urls import path

from customer import views

app_name = 'customer'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('orderhistory/', views.orderhistory, name='orderhistory'),
    path('logout/', views.auth_logout, name='logout'),
]
