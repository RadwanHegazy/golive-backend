from rest_framework import status, decorators
from rest_framework.response import Response
from ..serializers import RegisterSerializer

@decorators.api_view(['POST'])
def RegisterView (request) : 
    try :

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.get_tokens(),status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)