from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('customers/', views.customer , name='customers'),
    path('products/', views.product , name='products'),
    
]
