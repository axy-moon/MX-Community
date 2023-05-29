from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('search',views.search,name='search'),
    path('verify_account',views.verify,name='verify'),
    path('feed/placements',views.placement,name='placement')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


