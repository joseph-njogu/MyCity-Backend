from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .models import *
from .serializers import *

class UserCreate(generics.CreateAPIView):
	# authentication_classes = ()
	# permission_classes = ()
	serializer_class = UserSerializer

class LoginView(APIView):

	permission_classes = ()
	serializer_class = UserSerializer
	def post(self, request,):
		username = request.data.get("username")
		password = request.data.get("password")
		# user = authenticate(username=username, password=password)
		# if user:
		# 	return Response({"token": user.auth_token.key})
		# else:
		# 	return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (authentication.TokenAuthentication)
class ParkingViewSet(viewsets.ModelViewSet):
    queryset = ParkingInfo.objects.all().order_by('name')
    serializer_class = ParkingInfoSerializer
class ParkingInfoCreate(generics.CreateAPIView):
    # queryset = ParkingInfo.objects.create()
    serializer_class = ParkingInfoSerializer

class PlaceViewSet(viewsets.ModelViewSet):
	queryset = Place.objects.all().order_by('location')
	serializer_class = PlaceSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('served_date')
    serializer_class = BookingSerializer
class BookingCreate(generics.CreateAPIView):
    # queryset = Booking.objects.create()
    serializer_class = BookingSerializer