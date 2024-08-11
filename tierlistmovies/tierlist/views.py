from django.shortcuts import render
from django.http import HttpResponse
#from cinemagoerDetails import Cinemagoer

def teste(request):
    return HttpResponse("Olá, mundo!")
