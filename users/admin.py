from django.contrib import admin
from .models import User

class adminPanel (admin.ModelAdmin) : 
    list_display = ['full_name','email','picture',]
    
admin.site.register(User, adminPanel)