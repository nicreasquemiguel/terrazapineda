from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
 #   phone = models.IntegerField()
#    email = models.EmailField()


class Package(models.Model):
    id_package = models.IntegerField(primary_key = True)
    n_people = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length = 240)
    hours = models.CharField(max_length = 120)

class Extra(models.Model):
    id_extra = models.IntegerField(primary_key = True)
    description = models.CharField(max_length = 240)
    price = models.IntegerField()

class Venue(models.Model):
    id_venue =  models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 120)
    address = models.CharField(max_length = 360)


class Events(models.Model):
    id_events = models.IntegerField(primary_key = True)
    date = models.DateField()
    package = models.ForeignKey(Package, on_delete= models.CASCADE, related_name= "package")
    extras =  models.ForeignKey(Extra, on_delete= models.CASCADE, related_name="extras")
    client = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "client")
    admin = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "admin")
    venue = models.ForeignKey(Venue, on_delete = models.CASCADE, related_name = "venue")

    #created
    #modified 