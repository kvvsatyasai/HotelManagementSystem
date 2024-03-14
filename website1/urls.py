from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('login/',handleLogin, name='login'),
    path('register',register,name='register'),
    path('intro1/',introduction, name='intro'),
    path('intro1/fetch',retrieve,name='RET'),
    path('intro1/profile',profile,name='PROF'),
    path('logout/',handleLogout,name='logout'),
    path('intro1/booking/<int:room_id>',bookForm,name='bookForm'),
    path('intro1/booking/book',handleBooking,name='book'),
    path('intro1/maintenance',handleMaintainanceRequests,name='Mreq'),
    path('intro1/maintenance/emergency-procedures',emergencies,name='EP'),
    path('intro1/add-room',roomAdd,name='roomAdd'),
    path('intro1/add-room/add',handleAddRoom,name='add'),
    path('intro1/room-list',handleListRooms,name='roomList'),
    path('intro1/room-list/delete-room/<int:room_id>/',handleDeleteRoom,name='deleteRoom'),
    path('intro1/room-list/update-room/<int:room_id>/',handleUpdateRoom,name='updateRoom'),
    path('intro1/room-list/update-room/update/<int:room_id>/',updateForm,name='update'),
    path('intro1/inventorylist',handleInventory,name='INV'),
    path('intro1/inventory/item-handle',itemForm,name='itemForm'),
    path('intro1/inventory/add-item',handleaddItem,name='addItem'),
    path('intro1/inventory/delete-item/<int:item_id>/',deleteItem,name='deleteItem'),
    path('intro1/inventory/update-item-form/<int:item_id>/',itemUpdateForm,name='updateItem'),
    path('intro1/inventory/update-item/<int:item_id>/',handleUpdateItem,name='IU'),
    path('intro1/notice',noticeBoard,name='NB'),
    path('intro1/notice/add-notice',handleNotice,name='ann'),
    path('intro/announcement',announcement,name='AN'),
    path('intro1/notice/delete-notice/<int:notice_id>/',deleteNotice,name='deleteNotice'),
    path('intro1/notice/download-file/<int:notice_id>/',download_file,name='download'),
    path('check/',check,name='check'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


