from django.urls import path
from .views import index, movies_json
from .views import about
from . views import movies_index
from .views import movies_create
from .views import movies_store
from .views import movies_json

urlpatterns = [
    path('hello', index),
    path ('about', about),
    path ('movies', movies_index),
    path ('movies/create', movies_create),
    path ('movies/store', movies_store),
    path ('json/movies', movies_json)
]


