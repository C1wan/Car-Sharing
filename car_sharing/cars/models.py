from django.db import models

# Create your models here.
# TODO : Felder für Models überlegen

class Car(models.Model): 
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField(max_length=4)
    consumption_type = models.PositiveSmallIntegerField(max_length=4)
    latidude = models.DecimalField(max_digits=8)
    longitude = models.DecimalField(max_digits=8)
    
class Brand(models.Models):
    brand = brand = models.CharField(max_length=255)
    
class Model(models.Model):
    brand = models.CharField(max_length=255)
      
    def __str__(self):
        return str(self.name)
    
    #hier db relation beahcten make sollte eine eigene tabelle
    #haben und model und jahr auch usw...
    # verbrazch als enum machen gibts nur 3-4
    #baujahr auch