from django.contrib.auth.models import User, Group 
from rest_framework import serializers 
from rooms.models import Rooms,Service

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Group
        fields = ['url','name']

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
    services = ServicesSerializer(many=True)
    class Meta:
        model = Rooms
        fields = ['name','check_in_date','check_out_date','number_of_guests','room_number','services','price','active']