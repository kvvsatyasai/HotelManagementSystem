from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('login/',handleLogin, name='login'),
    path('register',register,name='register'),
    path('intro1/',introduction, name='intro'),
    path('intro1/fetch',retrieve,name='RET'),
    path('intro1/profile',profile,name='PROF'),
    path('logout/',handleLogout,name='logout'),
    path('intro1/booking',bookForm,name='bookForm'),
    path('intro1/booking/book',handleBooking,name='book'),
    path('intro1/maintenance',handleMaintainanceRequests,name='Mreq'),
    path('intro1/maintenance/emergency-procedures',emergencies,name='EP'),
    path('intro1/add-room',roomAdd,name='roomAdd'),
    path('intro1/add-room/add',handleAddRoom,name='add'),
    path('intro1/room-list',handleListRooms,name='roomList'),
]