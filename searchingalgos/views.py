from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request , 'searchingalgos/index.html')

    
def linearsearch(request):
    return render(request , 'searchingalgos/linearsearch/index.html')

def binarysearch(request):
    return render(request,'searchingalgos/binarysearch/index.html')





def performbinarysearch(request):
    arr = [1 , 4, 8 , 9 , 14 , 19 , 23 , 26 ,28 , 34 , 40 , 44 , 47 , 56 , 62 , 65 , 89 , 96 , 101 ]
    x = request.GET.get('binarysearchval' , 'default')
    x = int(x)
    result = binarySearch(arr, x)
    params = { 'list' : result['list'] , 'index' : result['mid'] , 'binarysearchvalue': x}
    
    return render(request , 'searchingalgos/binarysearch/result.html' , params)


def binarySearch(arr,element):
    liste = []
    low = 0
    high = len(arr)-1
     
    # initialize the 'if_found' variable with False.
    if_found = False
     
    # run the loop until if_found becomes True and
    # lower index is greater and higher index.
    while( low<=high and not if_found):
        # find the index of middle element
        mid = (low + high)//2
        liste.append([low , mid , high ])
         
        #If the middle element is the element we are looking for,
        # return the index of middle element  
        if arr[mid] == element :
            if_found = True
         
        else:
        # if the element is less than the middle element,
        # look for the element in the first part.
            if element < arr[mid]:
              # search for the element in array from index 0 to 
              # index mid-1
                high = mid - 1
             
            # if the element is greater than the middle 
            # element,look for the element in second part.
            else:
            # search for the element in array from index mid+1 to 
            # last index
                low = mid + 1
                 
    # if the element is found, get out of the loop and print the 
    # index
    if (if_found == True) :
       return({'mid': mid , 'list': liste})
    # if element is not in the array, run the below code
    else:
        return("Element {} Not found".format(element) , liste)
     



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