from distutils.command.upload import upload
from unicodedata import name
from django.db import models

# Create your models here.

# Heredan de una clase
class Movie(models.Model):
    name = models.CharField(max_length=255, null=True)
    poster = models.ImageField(upload_to = 'posters', null=True)
# crea una tabla