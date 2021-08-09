#This file is created by Lokesh
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'algos.html')

def submit(request):
    mytext = request.GET.get('text' , 'default')
    array = mytext.split(',')
    count = len(array)
    return HttpResponse(count)




