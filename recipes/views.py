from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.


def home(request):
    # Ele deve retornar um HTTP Response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'samuel',
        'sobrenome': 'Origa'
    })
