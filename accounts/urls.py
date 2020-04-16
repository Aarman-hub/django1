from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),

    path('', views.home , name='home'),
    path('customer/<str:pk_id>/', views.customer , name='customer'),
    path('products/', views.product , name='products'),

    path('order_form/<str:pk>/', views.orderForm , name='order_form'),
    path('update_form/<str:pk>/', views.updateForm , name='update_form'),
    path('delete_order/<str:pk>/', views.deleteForm, name='delete_order'),
    
]
