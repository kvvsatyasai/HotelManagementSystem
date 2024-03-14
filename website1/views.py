from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators  import login_required
# from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import *
from .decorators import unauthenticated_user,admin_only
import os


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


@unauthenticated_user
def introduction(request):
        if request.user.is_authenticated:
             my_user = User.objects.get(username=request.user)
             print(my_user)
             return render(request,'introduction.html') 

        else:
            messages.error(request,'Please Login First...!')
            return redirect('login')

    



@unauthenticated_user
def bookForm(request,room_id):
      if request.method == 'POST': 
        room_list = Rooms.objects.all()
        my_user = User.objects.get(username=request.user)
        get_room_no = get_object_or_404(Rooms,room_id=room_id)
        get_room_id = room_id
        room_no = get_room_no.Room_No
        name = my_user.username
        email = my_user.email
        return render(request,'book.html',{'name':name,'email':email,'rm':room_list,'room_no':room_no,'room_id':get_room_id})
      else:
            return HttpResponse('404 - Not Found for the booking...!')


@unauthenticated_user
def handleBooking(request):
        try:
            if request.method == 'POST':
                my_user = User.objects.get(username=request.user)
                count_user_booking = Booking.objects.all().filter(Customer_Name=my_user).count()
                print("Number of bookings done by user is: ",count_user_booking)
                rooms = request.POST.get('rooms_select')
                room_id = request.POST.get('room_id')
                get_room_id = get_object_or_404(Rooms,room_id=room_id)
                print(get_room_id.Room_No)
                print(rooms)
                print(request.POST)
                if count_user_booking < 1:
                     bookings = Booking.objects.create(status='Booked',Customer_Name=my_user,Room_No=Rooms.objects.get(Room_No=get_room_id.Room_No))
                     print(bookings)
                     bookings.save()
                     messages.success(request,'Room Booked Successfully...!')
                     return redirect('intro')
                else: 
                    messages.error(request,'You have already booked a room...!')
                    return redirect('intro')
            else:
                return HttpResponse('Not a Post method...!')
        except Rooms.DoesNotExist:
            print(Rooms.objects.all())
            return HttpResponse('404 - Not Found for the room...!')


@unauthenticated_user
def profile(request):
          my_user = User.objects.get(username=request.user)
          count_user_booking = Booking.objects.all().filter(Customer_Name=my_user).count()
          print("Number of bookings done by user is: ",count_user_booking)
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
          

@unauthenticated_user
def retrieve(request):
          rooms = Rooms.objects.all()
          print(rooms)
          try:
            print(rooms.values()[0]['capacity'])
            params = {'rm':rooms}
            return render(request,'roomsfetch.html',params)
          except IndexError:
            messages.success(request,'No rooms are available right now...!')
            return redirect('intro')


@unauthenticated_user
def handleMaintainanceRequests(request):
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
      
        print(user_room)
        return render(request,'maintananceRequest.html',{'user_room':user_room,'name':my_user.username})

        

def emergencies(request):
    return render(request,'emergency.html')


def roomAdd(request):
    return render(request,'addRoom.html')


@unauthenticated_user
def handleAddRoom(request):
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
            new_room.refresh_from_db()
            print("id of the room",new_room.room_id)
            messages.success(request,'Room Added Successfully...!')
            return redirect('roomAdd')
        else:
            return HttpResponse('Not the post method...')

@unauthenticated_user
def handleListRooms(request):

        rooms = Rooms.objects.all()
        size = rooms.count()
        print(rooms)
        return render(request,'listRooms.html',{'rm':rooms,'size':size})



@unauthenticated_user
def handleDeleteRoom(request,room_id):
        if request.method == 'POST':
            room = get_object_or_404(Rooms,room_id=room_id)
            room.delete()
            messages.success(request,'Room Deleted Successfully...!')
            return redirect('roomList')
        else:
            return HttpResponse('Not the post method...')

@unauthenticated_user
def updateForm(request,room_id):
    obj = get_object_or_404(Rooms,room_id=room_id)
    return render(request,'updateRoom.html',{'room_id':obj.room_id,'room_no':obj.Room_No,'room_type':obj.Room_Type,'room_price':obj.Room_Price,'capacity':obj.capacity})

def handleUpdateRoom(request,room_id):
    if request.method == 'POST':
        room = get_object_or_404(Rooms,room_id=room_id)
        room.Room_No = request.POST.get('room_no')
        room.Room_Type = request.POST.get('room_type')
        room.Room_Price = request.POST.get('room_price')
        room.capacity = request.POST.get('capacity')
        room.save()
        messages.success(request,'Room Updated Successfully...!')
        return redirect('roomList')
    else:
        return HttpResponse('Not the post method...')
   

@unauthenticated_user
def itemForm(request):
    return render(request,'addInventory.html')

@unauthenticated_user
def handleaddItem(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        item_type = request.POST.get('item_type')
        item_quantity = request.POST.get('item_quantity')

        print(item_name,item_type,item_price,item_quantity)
        items = Inventory.objects.all()
        for i in items:
            if i.item_name == item_name:
                messages.error(request,'Item which you want to add is already exists...!')

        new_item = Inventory.objects.create(item_name=item_name,item_type=item_type,item_price=item_price,item_quantity=item_quantity)
        new_item.save()
        new_item.refresh_from_db()
        print("id of the item",new_item.item_id)
        print(new_item.item_type)
        messages.success(request,'Item Added Successfully...!')
        return redirect('itemForm')
    else:
        return HttpResponse('Not the post method...') 

@unauthenticated_user
def handleInventory(request):
    items = Inventory.objects.all()
    return render(request,'inventory.html',{'items':items})


@unauthenticated_user
def deleteItem(request,item_id):
    if request.method == 'POST':
        item = get_object_or_404(Inventory,item_id=item_id)
        item.delete()
        messages.success(request,'Item Deleted Successfully...!')
        return redirect('INV')
    else:
        return HttpResponse('Not the post method...')

@unauthenticated_user
def itemUpdateForm(request,item_id):
    obj = get_object_or_404(Inventory,item_id=item_id)
    # context = {'item_name':obj.item_name,'item_type':obj.item_type,'item_price':obj.item_price,'item_quantity':obj.item_quantity}
    return render(request,'updateItem.html',{'item_id':obj.item_id,'item_name':obj.item_name,'item_type':obj.item_type,'item_price':obj.item_price,'item_quantity':obj.item_quantity})


@unauthenticated_user
def handleUpdateItem(request,item_id):
    if request.method == 'POST':
        item = get_object_or_404(Inventory,item_id=item_id)
        item.item_name = request.POST.get('item_name')
        item.item_type = request.POST.get('item_type')
        item.item_price = request.POST.get('item_price')
        item.item_quantity = request.POST.get('item_quantity')
        item.save()
        messages.success(request,'Item Updated Successfully...!')
        return redirect('INV')
    else:
        return HttpResponse('Not the post method...')



def noticeBoard(request):    
       return render(request,'notice.html')


def handleNotice(request):
    if request.method == 'POST':
        notice = request.POST.get('notice')
        notice_file = request.FILES.get('file')
        if notice_file:
            new_notice = Notice(notice=notice,file=notice_file)
            new_notice.save()
            messages.success(request,'Notice Added Successfully...!')
        print(notice,notice_file)
    return redirect('NB')

def announcement(request):
    notice= Notice.objects.all()
    print(notice.values())
    return render(request,'listAnnounce.html',{'notice':notice})

def deleteNotice(request,notice_id):
    if request.method == 'POST':
        notice = get_object_or_404(Notice,notice_id=notice_id)
        notice.delete()
        messages.success(request,'Notice Deleted Successfully...!')
        return redirect('AN')
    else:
        return HttpResponse('Not the post method...')

def download_file(request,notice_id):
    file_obj = get_object_or_404(Notice,notice_id=notice_id)

    with open(file_obj.file.path,'rb') as f:
        file_content = f.read()
     

    response = HttpResponse(file_content,content_type='application/force-download')

    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_obj.file.name)
    return response


def handleLogout(request):
    logout(request)
    request.session.flush() #remove session data from database
    return redirect('home')


def check(request):
    key = Rooms.objects.all()
    for k in range(len(key)):
        print(key[k].room_id)
    id = key.values()[2]['room_id']
    return HttpResponse(f"Id of Rooms are: {id}")