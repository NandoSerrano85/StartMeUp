from django.db import models


class User(model.Model):
    EIN = models.IntegerFields(primary_key=True, max_length=9)
    email = models.EmailField()
    business_name = models.CharField(max_length=300)
    principal = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    organization_type = models.CharField(max_length=30)
    business_type = models.CharField(max_length=30)
    phone = models.IntegerFields(max_length=10)
    

# Create your models here.

class Map(model.Model):
    class Meta:
        unique_together = (('zipcode', 'street'),)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerFields(primary_key=True, max_length=5)
    street = models.IntegerFields(max_length=10)
    county = models.CharField(max_length=25)
    latitude = models.IntegerFields(max_length=2)
    longitude = models.IntegerFields(max_length=2)

class Legislation(model.Model):
    county = models.ForeignKey(Map)
    city = models.ForeignKey(Map)
    state = models.ForeignKey(Map)
    legCode = models.TextField(primary_key=True, max_length=100) 
