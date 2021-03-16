from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Searching Algorithms")

    
def linearsearch(request):
    return HttpResponse("Linear Search")
