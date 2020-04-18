from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),

    path('', views.home , name='home'),
    path('userpage/', views.userPage , name='userpage'),
    path('accountsetting/', views.accountSetting , name='accountsetting'),
    path('customer/<str:pk_id>/', views.customer , name='customer'),
    path('products/', views.product , name='products'),

    path('order_form/<str:pk>/', views.orderForm , name='order_form'),
    path('update_form/<str:pk>/', views.updateForm , name='update_form'),
    path('delete_order/<str:pk>/', views.deleteForm, name='delete_order'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uid64>/<token>/', auth_views.PasswordResetCofirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
