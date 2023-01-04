from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('olá, aqui é o Django Fly')

# Create your views here.
#