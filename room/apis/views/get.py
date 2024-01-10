from rest_framework import decorators, status
from rest_framework.response import Response
from ...models import Room, Message, Ip
from ..serializers import RoomSerializer
from django.core.cache import cache


@decorators.api_view(['GET'])
def GetAll (request) : 
    try :
        
        if cache.get('rooms') is None : 
            rooms = Room.objects.order_by('-created_at')
            cache.set('rooms',rooms)
        else:
            rooms = cache.get('rooms')

        serializer = RoomSerializer(rooms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({
            'message' : f"an error accured : {error}"
        },status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['GET'])
def GetLive (request, live_id) :
    try : 
        try : 
            room = Room.objects.get(id=live_id)
        except Room.DoesNotExist : 
            return Response({
                "message" : 'not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        msgs = Message.objects.order_by('-id').values("text")
        data = {
            "room_id" : live_id,
            "messages" : msgs,
            "count_messages" : msgs.count(),
            "count_visitors" : room.visitors.all().count(),
        }
        return Response(data,status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)