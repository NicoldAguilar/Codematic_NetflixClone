from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Movie

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


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
    movies = Movie.objects.all()

    json_movies = []
    for o in movies:
        movie = {
            "id": o.id,
            "tittle": o.name
        }
        json_movies.append(movie)

    return JsonResponse(json_movies, safe=False)