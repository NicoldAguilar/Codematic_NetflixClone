from django.urls import path, include
from .views import MovieViewSet, index, movies_json
from .views import about
from . views import movies_index
from .views import movies_create
from .views import movies_store
from .views import movies_json

from rest_framework import routers



router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

# http://dominio.com/api/movies GET (ALL)
# http://dominio.com/api/movies POST (CREAR)
# http://dominio.com/api/movies GET (1 ELEMENTO)
# http://dominio.com/api/movies PUT (ACTUALIZAR)
# http://dominio.com/api/movies DELETE ( ELIMINAR)

urlpatterns = [
    path ('', include(router.urls)),
    path('hello', index),
    path ('about', about),
    #path ('movies', movies_index),
    #path ('movies/create', movies_create),
    #path ('movies/store', movies_store),
    path ('json/movies', movies_json),
]


