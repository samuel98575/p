from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.


def home(request):
    # Ele deve retornar um HTTP Response
    return HttpResponse('Home 1')


def sobre(request):
    # Ele deve retornar um HTTP Response
    return HttpResponse('sobre 1')


def contato(request):
    # Ele deve retornar um HTTP Response
    return HttpResponse('contato 1')
