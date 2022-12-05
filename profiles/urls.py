from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('login',views.login,name='login')
]
