from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from ..serializers import ProfileSerializer

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def ProfileView (request) : 
    try :

        serializer = ProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)