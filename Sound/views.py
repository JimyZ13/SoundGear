from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hellow World")

def text(request):
    return HttpResponse("Testing")