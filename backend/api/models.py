from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book (models.Model):
    Title = models.CharField(max_length=250)
    Author = models.CharField(max_length=250)
    Pub_Place = models.CharField(max_length=250)
    Pub_Year = models.CharField(max_length=20)
    Publisher = models.CharField(max_length=250)
    Repository = models.CharField(max_length=250)
    Call_Num = models.CharField(max_length=250)
    Vol_Num = models.Int





class Evidence(models.Model):

class Provenance_Person(models.Model):

class Image (models.Model):
