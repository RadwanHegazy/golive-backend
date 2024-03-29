from rest_framework import serializers
from ..models import Room, Message
from users.models import User
from django.contrib.humanize.templatetags import humanize
import datetime

class CreateBySerializer  (serializers.ModelSerializer) : 
    class Meta :
        model = User
        fields = ('full_name','picture',)

class RoomSerializer (serializers.ModelSerializer) : 
    created_by = CreateBySerializer()
    class Meta :
        model = Room
        fields = ["id","created_at",'title','created_by']

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['created_at'] = humanize.naturaltime(instance.created_at)
        return data

class MessageSerializer (serializers.ModelSerializer) : 
    
    class Meta : 
        model = Message
        fields = ("id",'text')