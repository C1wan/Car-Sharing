from django.db import models

# Create your models here.
# TODO : Felder für Models überlegen

class Car(models.Model): 
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField(max_length=4)
    
    
    #hier db relation beahcten make sollte eine eigene tabelle
    #haben und model und jahr auch usw...
    # verbrazch als enum machen gibts nur 3-4
    #baujahr auch