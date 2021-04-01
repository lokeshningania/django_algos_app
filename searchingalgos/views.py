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
    arr = [1 , 4, 8 , 9 , 14 , 19 , 23 , 26 ,28 , 34 , 40 , 44 , 47 , 56 , 62 , 65 , 89 , 96 ]
    x = request.GET.get('binarysearchval' , 'default')
    x = int(x)
    resultlist = []
    result = binarySearch(arr, 0, len(arr)-1, x)
    params = {'binarysearchval': x , 'index' : result}
    return render(request , 'searchingalgos/binarysearch/result.html' , params)


# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):

	# Check base case
	if r >= l:

		mid = l + (r - 1) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid
		
		# If element is smaller than mid, then it
		# can only be present in left subarray
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)

		# Else the element can only be present
		# in right subarray
		else:
			return binarySearch(arr, mid + 1, r, x)

	else:
		# Element is not present in the array
		return -1




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