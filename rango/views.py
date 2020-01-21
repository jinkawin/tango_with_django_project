from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='/rango/about'>Go to About</a>")

def about(request):
    return HttpResponse("This is about page!")