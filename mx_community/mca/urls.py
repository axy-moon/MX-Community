from django.urls import path
from . import views

urlpatterns = [
    path('feed/',views.feed,name='feed'),
    path('register/',views.register,name='register'),    
    path('login/',views.login,name='login'),
    path('tokens/',views.token,name='tokens'),
    path('',views.home,name='home'),
    path('logout',views.logout,name = 'logout'),
    path('messages',views.messages,name='messages'),
    path('profile',views.profiles,name='profile'),
    path('profile_setup',views.prosetup,name='profile_setup'),
    path('search',views.search,name='search')
    
]

