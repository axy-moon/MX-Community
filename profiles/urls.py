from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('feed',views.feed,name='feed'),
    path('messages',views.messages,name='messages'),
    path('search',views.search,name='search'),
    path('tokens',views.tokens,name='tokens')
    
]
