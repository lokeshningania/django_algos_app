#This file is created by Lokesh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Home Page")
    
def countdown(request):
    return render(request , 'countdown.html')


def submit(request):
    mytext = request.GET.get('text' , 'default')
    array = mytext.split(',')
    count = len(array)
    return HttpResponse(count)




