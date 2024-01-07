from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.

book = Booking.objects.first()
        #   for i in book:
room = Rooms.objects.get(Room_No=book.Room_No)
room_list = Rooms.objects.first()
print(book.Room_No)