from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('olá django')

# Create your views here.
