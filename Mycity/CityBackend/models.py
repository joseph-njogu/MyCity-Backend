from django.db import models
import datetime

CHOICES_TYPE = (
    ("1","Disabled"),
    ("2","NotDisabled")
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
    name = models.CharField(max_length=20)
    coord = models.PointField(blank=True, null=True)
    
    def __str__(self):
          return self.name
  
class ParkingInfo(models.Model):
    capacity = models.IntegerField()
    location = models.PointField(blank=True, null=True)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=20,choices=CHOICES_TYPE, default=1)

    def __str__(self):
            return self.capacity
class Packing(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    parkinginfo = models.ForeignKey(ParkingInfo, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)