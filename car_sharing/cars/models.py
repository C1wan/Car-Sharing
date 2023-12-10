from django.db import models
import datetime

# Create your models here.
# TODO : Felder für Models überlegen


class Brand(models.Models):
    brand = brand = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
            return str(self.brand)

class Model(models.Models):
    model = brand = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
            return str(self.model)
        
class Consumption_Type(models.Models):
    consumption_type = models.CharField(max_length=100)
    def __str__(self):
            return str(self.consumption_type)
        
class Color(models.Models):
    color = models.CharField(max_length=100)
    def __str__(self):
            return str(self.color)

class Year(models.Models):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    
    year = models.IntegerField(_('year'),choices=YEAR_CHOICES, default=datetime.datetime.now().year,blank=False)
    def __str__(self):
            return str(self.year)

class Car(models.Model): 
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,blank=False)
    model = models.ForeignKey(Model,on_delete=models.PROTECT,blank=False)
    year = models.ForeignKey(Year,on_delete=models.PROTECT,blank=False)
    consumption_type = models.ForeignKey(Consumption_Type,on_delete=models.PROTECT,blank=False)
    color = models.ForeignKey(Color,on_delete=models.PROTECT,blank=False)
    latidude = models.DecimalField(max_digits=8)
    longitude = models.DecimalField(max_digits=8)
    

    

    
    #hier db relation beahcten make sollte eine eigene tabelle
    #haben und model und jahr auch usw...
    # verbrazch als enum machen gibts nur 3-4
    #baujahr auch
    # TODO : OWNER HINZUFÜGEN