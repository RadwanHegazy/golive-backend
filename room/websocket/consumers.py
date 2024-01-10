from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from room.models import Room, Message
from room.apis.serializers import MessageSerializer
import json


class RoomConsumer (WebsocketConsumer) : 

    def connect(self):

        self.room_id = self.scope['url_route']['kwargs']['room_id']
        
        try : 
            self.room = Room.objects.get(id=self.room_id)
        except Room.DoesNotExist : 
            self.close()
            return
        
        self.group_name = f"room_{self.room_id}"

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        messages = Message.objects.filter(room=self.room)
        msg_serializer = MessageSerializer(messages, many=True)

        data = {
            'room_messages' : msg_serializer.data
        }

        self.send(text_data=json.dumps(data))


    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        json_data = json.loads(text_data)
        msg_text = json_data['message']
        Message.objects.create(room=self.room,text=msg_text).save()

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type' : 'sendMsg',
                'data' : json_data
            }
        )
        

    def sendMsg (self, event) :
        self.send(text_data=json.dumps(event['data']))