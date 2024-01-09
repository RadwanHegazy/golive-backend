from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ...models import Room
from ..serializers import RoomSerializer

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.IsAuthenticated])
def CreateLive (request): 
    try : 
        user = request.user

        if Room.objects.filter(created_by=user).exists() : 
            return Response({
                'message' : 'there is already live'
            },status=status.HTTP_400_BAD_REQUEST)
        
        title = request.data.get('title',None)
        
        if title is None or title == "" : 
            return Response({"message" : "title filed can't be empty"},status=status.HTTP_400_BAD_REQUEST)
        
        room = Room.objects.create(
            title = title,
            created_by = user
        )

        return Response({'id' : room.id},status=status.HTTP_200_OK)
    
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)