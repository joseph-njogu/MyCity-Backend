from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import *;

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = '__all__'

class ParkingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parking
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'email', 'password')

	def create(self, validated_data):
		user = User(
		first_name=validated_data['first_name'],
		last_name=validated_data['last_name'],
		email=validated_data['email'],
		username=validated_data['username'])

		user.set_password(validated_data['password'])
		user.is_staff=True
		user.save()
		Token.objects.create(user=user)
		return user
class ParkingInfoSerializer(serializers.ModelSerializer):
    	class Meta:
            model = ParkingInfo
            fields = '__all__'
class BookingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ('status', 'ratings', 'plate', 'amount', 'parkinginfo')