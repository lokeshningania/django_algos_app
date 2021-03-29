from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request , 'searchingalgos/index.html')

    
def linearsearch(request):
    return render(request , 'searchingalgos/linearsearch/index.html')

def performlinearsearch(request):
    data = request.GET.get('array' , 'default')
    print("Function working")
    params = {'array': data}
    return render(request , 'searchingalgos/linearsearch/result.html' , params)