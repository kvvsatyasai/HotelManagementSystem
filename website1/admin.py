from django.contrib import admin
from .models import *
# Register your models here.
# class RegisterAdmin(admin.ModelAdmin):
    # list_display = ('Name','E_mail','password') #-> to display the fields in admin page.

admin.site.register(Rooms)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(maintainanceRequest)