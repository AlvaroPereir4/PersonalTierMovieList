from django.shortcuts import render
#from cinemagoerDetails import Cinemagoer

def index(request):
    return render(request, 'index.html')
