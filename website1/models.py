from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    Room_No = models.CharField(max_length=50)
    Room_Type = models.CharField(max_length=50,choices=CATEGORY)
    Room_Price = models.CharField(max_length=50)
    capacity = models.IntegerField(default=3)
    def __str__(self):
        return self.Room_No

class Booking(models.Model):    
    status = models.CharField(max_length=50,choices=(('Booked','Booked'),('Not Booked','Not Booked')))
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