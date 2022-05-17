from unicodedata import category
from django.db import models

choices = (
    ("Maimed"),
    ("Normal"),
)
class UserData(models.Model):
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=10)

class Place(models.Model):
    name = models.CharField(max_length=20)
    coord = models.PointField(blank=True, null=True)
    
    def __str__(self):
          return self.name
  
class Parking(models.Model):
    capacity = models.IntegerField()
    location = models.PointField(blank=True, null=True)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=20,choices, default=None)