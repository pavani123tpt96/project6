from django.shortcuts import render

from django.http import *

# Create your views here.

  

def first (request):
    return HttpResponse ('this is my first view function')

def tirupathi (request):
    return HttpResponse ('<h1><marquee>tirupathi is one of the most visited pilgrimage center in india</marquee></h1>')
