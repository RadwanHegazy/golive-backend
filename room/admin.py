from django.contrib import admin
from .models import Room, Message



class RoomPanel (admin.ModelAdmin) : 
    list_display = ['id','created_by','title','created_at']

class MessagePanel (admin.ModelAdmin) : 
    list_display = ['text','room']


# register to admin panel

admin.site.register(Message, MessagePanel)

admin.site.register(Room, RoomPanel)
