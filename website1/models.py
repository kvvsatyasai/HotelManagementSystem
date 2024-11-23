from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.  
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    dp = models.ImageField(blank=True,upload_to='profile_pics/')
    def __str__(self):
        return self.user.username

class Rooms(models.Model):
    CATEGORY = (
        ('DELUXE','DELUXE'),('LUXURY','LUXURY'),('PREMIUM','PREMIUM')
    )
    room_id = models.AutoField(primary_key=True)
    Room_No = models.CharField(max_length=50,unique=True)
    Room_Type = models.CharField(max_length=50,choices=CATEGORY)
    Room_Price = models.CharField(max_length=50) 
    capacity = models.IntegerField(default=3)
    def __str__(self):
        return self.Room_No

class Booking(models.Model):    
    status = models.CharField(max_length=50,choices=(('Booked','Booked'),('Not Booked','Not Booked')),default='Not Booked')
    book_id = models.AutoField(primary_key=True)
    Customer_Name = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Room_No = models.ForeignKey(Rooms,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.Customer_Name} - {self.Room_No} - {self.status}"

class maintainanceRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    Customer_Name = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Room_No = models.ForeignKey(Rooms,on_delete=models.SET_NULL,null=True)
    issue = models.TextField()
    date_of_request = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.Customer_Name} - {self.Room_No}"



class Inventory(models.Model):
    CATEGORY = (
        ('Electronics','Electronics'),('Furniture','Furniture'),('Stationary','Stationary'),('Grocery','Grocery'))
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_type = models.CharField(max_length=50,choices=CATEGORY)
    item_price = models.CharField(max_length=50)
    item_quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.item_name

class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    notice = models.TextField()
    file = models.FileField(blank=True,upload_to='notices/',null=True)
    date_of_notice = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.notice_id}-{self.notice}'