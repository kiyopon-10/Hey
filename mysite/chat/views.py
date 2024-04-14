from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room


# Create your views here.

def main_view(request):
    context = {}
    
    return render(request, 'chat/main.html', context=context)


@api_view(['GET'])
def check_room_existence(request):
    room_code = request.query_params.get('room_code', None)
    if room_code is not None:
        try:
            room = Room.objects.get(room_code=room_code)
            return Response({'exists': True}, status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            return Response({'exists': False}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'room_code parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

