# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #Acá tengo que subir el archivo
    #return HttpResponse("Hello, you're home.")
    return render(request, 'home.html')