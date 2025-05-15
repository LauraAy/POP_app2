from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book (models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    creation_place = models.CharField(max_length=250)
    creation_date = models.IntegerField(max_length=4)
    date_description = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    repository = models.CharField(max_length=250)
    call_num = models.CharField(max_length=250)
    vol_num = models.IntegerField(max_length=5)
    catalog_url = repository = models.URLField(blank=True, null=True)
    other_id = models.CharField(max_length=250)
    other_id_type = models.CharField(max_length=250)
    geo_location = models.CharField(max_length=250)
    sammelband = models.BooleanField(blank=True, null=True)
    acq_source = models.CharField(max_length=250)



class Evidence(models.Model):
    transcription = models.TextField
    translation = models.TextField
    description = models.textField
    language = models.CharField(max_length=250)
    evidence_format = models.models.CharField(max_length=250)
    location_book = models.CharField(max_length=250)
    content_type = models.CharField(max_length=250)
    date = models.IntegerField(max_length=4)
    date_start = models.IntegerField(max_length=4)
    date_end = models.IntegerField(max_length=4)
    date_description = models.CharField(max_length=250)
    name_associated = models.CharField(max_length=250)
    place_associated = models.CharField(max_length=250)
    citations = models.TextField

    
    




    


class Provenance_Person(models.Model): 

class Image (models.Model):
