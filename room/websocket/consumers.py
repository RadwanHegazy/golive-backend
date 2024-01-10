from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class RoomConsumer (WebsocketConsumer) : 

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        print('recived : ',text_data)