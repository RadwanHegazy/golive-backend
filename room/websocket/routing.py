from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('room/',consumers.RoomConsumer.as_asgi()),
]