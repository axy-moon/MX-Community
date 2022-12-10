from django.urls import path
from . import views

urlpatterns = [
    path('',views.feed,name='feed'),
    path('register',views.register,name='register'),    
    path('login',views.login,name='login'),
    path('tokens',views.tokens,name='tokens')
    #path('feed',views.feed,name='feed'),
    #path('messages',views.messages,name='messages'),
    #path('search',views.search,name='search'),
    
]

