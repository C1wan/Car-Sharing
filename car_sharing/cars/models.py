from django.db import models
import datetime

# Create your models here.
# TODO : Felder für Models überlegen


class Brand(models.Model):
    brand  = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
         return str(self.brand)

class Car_Model(models.Model):
    car_model =  models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
            return str(self.car_model)
        
class Consumption_Type(models.Model):
    consumption_type = models.CharField(max_length=100)
    def __str__(self):
            return str(self.consumption_type)
        
class Color(models.Model):
    color = models.CharField(max_length=100)
    def __str__(self):
            return str(self.color)

class Year(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    
    
    year = models.IntegerField(('year'),choices=YEAR_CHOICES, default=datetime.datetime.now().year,blank=False)
    def __str__(self):
            return str(self.year)

class Car(models.Model): 
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,blank=False)
    car_model = models.ForeignKey(Car_Model,on_delete=models.PROTECT,blank=False)
    year = models.ForeignKey(Year,on_delete=models.PROTECT,blank=False)
    consumption_type = models.ForeignKey(Consumption_Type,on_delete=models.PROTECT,blank=False)
    color = models.ForeignKey(Color,on_delete=models.PROTECT,blank=False)
    latidude = models.DecimalField(max_digits=8,decimal_places=5)
    longitude = models.DecimalField(max_digits=8,decimal_places=5)
    

    

    
    #hier db relation beahcten make sollte eine eigene tabelle
    #haben und model und jahr auch usw...
    # verbrazch als enum machen gibts nur 3-4
    #baujahr auch
    # TODO : OWNER HINZUFÜGEN