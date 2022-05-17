from django.contrib import admin
from .models import *

@admin.register(Place)
@admin.register(UserData)
@admin.register(Packing)
@admin.register(ParkingInfo)

class PlaceAdmin(admin.OSMGeoAdmin):
   pass
