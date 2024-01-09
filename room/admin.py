from django.contrib import admin
from .models import Ip, Room, Message


# create panels

class IpPanel (admin.ModelAdmin) : 
    list_display = ['ip']

class RoomPanel (admin.ModelAdmin) : 
    list_display = ['created_by','title','created_at']

class MessagePanel (admin.ModelAdmin) : 
    list_display = ['text','room']


# register to admin panel

admin.site.register(Message, MessagePanel)

admin.site.register(Room, RoomPanel)

admin.site.register(Ip, IpPanel)