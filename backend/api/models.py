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
    comment = models.TextField
    who_id = models.BooleanField(blank=True, null=True)
    where_id = models.BooleanField(blank=True, null=True)
    when_id = models.BooleanField(blank=True, null=True)

class Names(models.Model):
    name = models.CharField(max_length=250)
    date_start = models.IntegerField(max_length=4)
    date_end = models.IntegerField(max_length=4)
    date_description = models.CharField(max_length=250)
    viaf_id = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    description = models.TextField

class Places(models.Model):
    location_name = models.CharField(max_length=250)
    location_type = models.CharField(max_length=250)
    lon = models.FloatField()
    lat = models.FloatField()

class Provenance_Agent(models.Model): 
    provenance_role = models.CharField(max_length=250)
    comment = models.TextField

class Image (models.Model):
    image_file_name = models.CharField(max_length=250)
    image_file_size = models.CharField(max_length=250)

