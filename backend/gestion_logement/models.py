from django.db import models

from logement import settings

class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default=f'${settings.IMAGE_URL}/default.jpg')
    
class Building(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    cp = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    photo = models.ManyToManyField(Photo)
    
    class Meta:
        ordering = ['name']

class Appartment(models.Model):
    
    types = {
        "APP": "APPARTEMENT",
        "HOU": "HOUSE",
    }
    name = models.CharField(max_length=100)
    floor = models.IntegerField(default=0)
    number = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    cp = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=types)
    building = models.ForeignKey(
        Building, 
        on_delete=models.CASCADE,
        null=True
        )
    photo = models.ManyToManyField(Photo)
    class Meta:
        ordering = ['name']
