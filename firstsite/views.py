#This file is created by Lokesh
from django.http import HttpResponse

def index(request):
    a=56
    b=34
    c = a+b
    return HttpResponse(c)
    