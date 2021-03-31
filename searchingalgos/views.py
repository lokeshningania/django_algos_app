from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request , 'searchingalgos/index.html')

    
def linearsearch(request):
    return render(request , 'searchingalgos/linearsearch/index.html')

def binarysearch(request):
    return render(request,'searchingalgos/binarysearch/index.html')



def performlinearsearch(request):
    array = [34,32,56,45,36,90,23,12,98,27,75,16,19,31,11,18,14,29,63]
    x = request.GET.get('searchval' , 'default')
    print("Function working")
    for i in range(0,len(array)):
        x = int(x)
        if x == array[i]:
            y = str(i)
            msg = 'Given number is present at index => '+ y
            print("The number ",x," is present on index " , i)
            break
        i+=1
    if i == len(array):
        msg = "Given element is not present in the array"
        print("Worst Case")

    if i == 0:
        msg = "Given element is found at 1st position"
        print("Best Case")

    params = {'searchval': x , 'position': msg , 'index': i}
    return render(request , 'searchingalgos/linearsearch/result.html' , params)