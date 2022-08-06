from distutils.command.upload import upload
from unicodedata import name
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name

# Create your models here.
# Heredan de una clase
class Movie(models.Model):
    name = models.CharField(max_length=255, null=True)
    poster = models.ImageField(upload_to = 'posters', null=True)
    gender = models.ForeignKey(Gender, on_delete = models.CASCADE, null=True) #conexion con la otra tabla
    player = models.ManyToManyField(Player)
    def __str__(self): 
        return self.name
# crea una tabla
