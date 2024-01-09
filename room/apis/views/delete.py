from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ...models import Room


@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAuthenticated])
def DeleteLive (request, live_id) : 
    try :
        try : 
            live = Room.objects.get(id=live_id)
        except Room.DoesNotExist :
            return Response({
                'message' : 'not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        if live.created_by != request.user :
            return Response({
                'message' : "permission error"
            },status=status.HTTP_403_FORBIDDEN)

        live.delete()

        return Response({
            "message" : "deleted successfully"
        },status=status.HTTP_200_OK)
    
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)