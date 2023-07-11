from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html', {

    }) 

def reglamento(request):
    return render (request, 'reglamento.html', {

    }) 

def precios(request):
    return render (request, 'precios.html', {

    }) 

def fotos(request):
    return render (request, 'fotos.html', {

    }) 

def comollegar(request):
    return render (request, 'comollegar.html', {

    }) 

def preguntasfrecuentes(request):
    return render (request, 'preguntasfrecuentes.html', {

    }) 