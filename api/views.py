from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Movie, Player

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework import serializers, viewsets

def index(request):
    return HttpResponse('Hola Mundo')

def about(request):
    return HttpResponse('Sobre mi')

def movies_index(request):
    movies = Movie.objects.all() #all() trae todo los datos y lo almacena en la variable 
    for movie in movies: #for
        print(movie)
    return render(request,"movies/index.html", {'abc': "Hola Mundo", 'movies': movies}) 
                #lee un archivo cualquiera y lo transforma en un string
                #Se envia y recibe el primer request

def movies_create(request):
    return render (request, 'movies/create.html')

def movies_store(request):
    print(request.POST["titulo"])
    print(request.FILES)

    #Guardar pelicula (nombre o chars)
    movie = Movie()
    movie.name = request.POST["titulo"]
    movie.save()

    #Guardar archivos
    image = request.FILES['image']
    path = default_storage.save("posters/" + image.name, ContentFile(image.read())) #guarda en la carpeta del proyecto pero no en la base de datos
    
    return HttpResponse("Vamos a guardar la pelicula")    
    
def movies_json (request):

    movies = Movie.objects.select_related('gender').all()

    json_movies = []
    for o in movies:
        movie = {
            "id": o.id,
            "tittle": o.name,
            "gender": o.gender.name if o.gender else '-' #para evitar que genero siendo null colapse la api
        }
        json_movies.append(movie)

    return JsonResponse(json_movies, safe=False)

#Permite serializar un objeto, en termino simple, transforma un objeto comple
class MovieSerializer(serializers.ModelSerializer):

    #No olvidar agregar en los fields de la clase meta
    gender_name = serializers.SerializerMethodField() #no está en la base de datos
    players = serializers.SerializerMethodField()

    def get_gender_name (self, obj):
        return obj.gender.name if obj.gender else None #controla el gender que no existe 

    def get_players (self,obj):
        return [x.name for x in obj.player.all()] #transforma el arreglo en un string 

    class Meta:
        model = Movie
        fields = ['id', 'name', 'poster', 'gender_name', 'players']

#Configura el CRUD
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer