from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h1>this is app2 first view')
def second(request):
    return HttpResponse('this is app2 second view')
