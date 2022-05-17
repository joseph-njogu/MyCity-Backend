from rest_framework import serializers
from .models import *;

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = '__all__'

class ParkingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parking
		fields = '__all__'

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = fields = ('fname', 'lname', 'username','email')