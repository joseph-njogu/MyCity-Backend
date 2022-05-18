from django.db import models
import datetime
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

CHOICES_TYPE = (
    ("Busy","Busy"),
    ("Available","Available")
)
# class UserData(models.Model):
#     fname = models.CharField(max_length=120)
#     lname = models.CharField(max_length=120)
#     username = models.CharField(max_length=120)
#     email = models.EmailField(max_length=120)
#     password = models.CharField(max_length=10)
#
#     def __str__(self):
#             return self.username

class Place(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    def __str__(self):
          return self.city
  
class ParkingInfo(models.Model):
    capacity = models.IntegerField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=20,choices=CHOICES_TYPE, default=1)

    def __str__(self):
            return self.name
status_choices = (
    ("1", "In Progress"),
    ("2", "Completed")
)
Rating_choices = (
    ("1", "Good"),
    ("2", "Average"),
    ("3", "Bad")
)
class Parking(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parkinginfo = models.ForeignKey(ParkingInfo, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    bookingdate = models.DateTimeField(auto_now=True)

class Bookings(models.Model):
    status = models.CharField(max_length=20, choices=status_choices, default=1)
    ratings = models.CharField(max_length=20, choices=Rating_choices, default=1)
    plate = models.CharField(max_length=8)
    served_date = models.DateTimeField(auto_now=True)
    parkinginfo = models.ForeignKey(ParkingInfo, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
            return self.plate