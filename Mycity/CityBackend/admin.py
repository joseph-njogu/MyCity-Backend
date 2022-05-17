from django.contrib import admin
from .models import *

@admin.register(Place)
@admin.register(UserData)

class PlaceAdmin(admin.OSMGeoAdmin):
   pass
