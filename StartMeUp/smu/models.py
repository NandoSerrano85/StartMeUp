from django.db import models


class User(model.Model):
    EIN = models.IntegerFields(primary_key=True, max_length=9)
    email = models.EmailField()
    business_name = models.CharField(max_length=300)

# Create your models here.
