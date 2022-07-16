from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Movie) #decorador
class MovieAmin(admin.ModelAdmin):
    pass