from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hola Mundo')

def about(request):
    return HttpResponse('Sobre mi')