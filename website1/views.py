from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators  import login_required
# from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def home_page(request):
    return render(request,'home.html')


def handleLogin(request):
    if request.method == 'POST':
        login_name = request.POST['name']
        login_password = request.POST['pwd']
        
        user = authenticate(request, username=login_name, password=login_password)

        if user is not None:
            login(request,user)
            return redirect('intro')
        else:
            messages.error(request,'Invalid Login credentials...!')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        phone = request.POST.get('cont')
        password = request.POST.get('pwd')
        print(name,email,phone,password)
        new_user = User.objects.create_user(name,email,password)
        new_user.first_name = phone
        new_user.save() 
        print(new_user.id)
        messages.success(request,'Account Created Successfully....')
        return redirect('login')
    else:
        return HttpResponse('404 - Not Found')



def introduction(request):
        if request.user.is_authenticated:
             my_user = User.objects.get(username=request.user)
             print(my_user)
             return render(request,'introduction.html') 

        else:
            messages.error(request,'Please Login First...!')
            return redirect('login')

    
room_list = Rooms.objects.all()



def bookForm(request):
    if request.user.is_authenticated: 
        my_user = User.objects.get(username=request.user)
        name = my_user.username
        email = my_user.email
        return render(request,'book.html',{'name':name,'email':email,'rm':room_list})
    else:
        return HttpResponse('404 - Not Found')


def handleBooking(request):
    if request.user.is_authenticated: 
        my_user = User.objects.get(username=request.user)
        if request.method == 'POST':
            rooms = request.POST.get('rooms_select')
            print(rooms)
            print(request.POST)
            bookings = Booking.objects.create(status='Booked',Customer_Name=my_user,Room_No=Rooms.objects.get(Room_No=rooms))
            print(bookings)
            bookings.save()
        return redirect('intro')
    else:
        return HttpResponse('404 - Not Found')


def profile(request):
    if request.user.is_authenticated:
          my_user = User.objects.get(username=request.user)

          try:
             bookings = Booking.objects.get(Customer_Name=my_user)
             room = Rooms.objects.all().filter(Room_No=bookings.Room_No)
             print(room.values()[0]['Room_Price'])
             params = {'name':my_user.username,'email':my_user.email,'phone':my_user.first_name,'bookings_room':bookings.Room_No,
             'bookings_status':bookings.status,'bookings_id':bookings.book_id,'room_price':room.values()[0]['Room_Price'], 
             'room_type':room.values()[0]['Room_Type'], 'room_capacity':room.values()[0]['capacity']}
             return render(request,'profile.html',params)

          except Booking.DoesNotExist:
             count_room = Booking.objects.all().filter(status='Booked').count() 
             print(count_room)
             return render(request,'error.html',{'name':my_user.username,'email':my_user.email,'phone':my_user.first_name})      
          
    else:
        return HttpResponse('404 - Not Found')


def retrieve(request):
    if request.user.is_authenticated:
          rooms = Rooms.objects.all()
          print(rooms)
        #   avl_rooms = room_list.filter(status='Not Booked')
          print(rooms.values()[0]['capacity'])
        #   prof = Customer.objects.all()

        #   image = prof.values()[0]['dp']
          params = {'rm':rooms}
          return render(request,'roomsfetch.html',params)
    else:
        return HttpResponse('404 - Not Found')


def handleMaintainanceRequests(request):
    if request.user.is_authenticated:
        my_user = User.objects.get(username=request.user)
        user_room = None
        try:
             bookings = Booking.objects.get(Customer_Name=my_user)
             user_room = bookings.Room_No
             if request.method == 'POST':
                issue = request.POST.get('issue') 
                requests = maintainanceRequest.objects.create(Customer_Name=my_user,Room_No=user_room,issue=issue)
                print(requests)
                requests.save()
            
        except Booking.DoesNotExist:
            messages.error(request,'You have not booked any room yet...!')
            return redirect('intro')
            # print(rooms)
            # print(issue)
            # print(request.POST)
      
        print(user_room)
        return render(request,'maintananceRequest.html',{'user_room':user_room,'name':my_user.username})

        
    else:
        return HttpResponse('404 - Not Found')

def emergencies(request):
    return render(request,'emergency.html')


def roomAdd(request):
    print(room_list)
    return render(request,'addRoom.html')


def handleAddRoom(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            room_no = request.POST.get('room_no')
            room_type = request.POST.get('room_type')
            room_price = request.POST.get('room_price')
            capacity = request.POST.get('capacity')
            print(room_no,room_type,room_price,capacity)
            rooms = Rooms.objects.all()
            for i in rooms:
                if i.Room_No == room_no:
                    messages.error(request,'Room which you want to add is already exists...!')
                    return redirect('roomAdd')
            new_room = Rooms.objects.create(Room_No=room_no,Room_Type=room_type,Room_Price=room_price,capacity=capacity)
            new_room.save()
            messages.success(request,'Room Added Successfully...!')
            return redirect('roomAdd')
        else:
            return HttpResponse('Not the post method...')
    else:
        return HttpResponse('404 - Not Found')

def handleListRooms(request):
    if request.user.is_authenticated:
        rooms = Rooms.objects.all()
        size = rooms.count()
        print(rooms)
        return render(request,'listRooms.html',{'rm':rooms,'size':size})
    else:
        return HttpResponse('404 - Not Found')
   


def handleLogout(request):
    logout(request)
    request.session.flush() #remove session data from database
    return redirect('home')