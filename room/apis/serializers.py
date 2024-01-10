from rest_framework import serializers
from ..models import Room, Message
from users.models import User

class CreateBySerializer  (serializers.ModelSerializer) : 
    class Meta :
        model = User
        fields = ('full_name','picture',)

class RoomSerializer (serializers.ModelSerializer) : 
    created_by = CreateBySerializer()
    class Meta :
        model = Room
        fields = ["id","created_at",'title','created_by']


class MessageSerializer (serializers.ModelSerializer) : 
    
    class Meta : 
        model = Message
        fields = ("id",'text')