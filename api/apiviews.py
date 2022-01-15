from rest_framework.views import APIView 
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

from rooms.models import Rooms 
from .serializers import RoomsSerializer 
class RoomList(APIView):
    def get(self,request):
        rooms = Rooms.objects.all() 
        data = RoomsSerializer(rooms,many=True).data 
        return Response(data)

class RoomDetails(APIView):
    def get(self,request,pk):
        room =  get_list_or_404(Rooms, pk=pk)
        data = RoomsSerializer(room,many=True).data
        return Response(data)