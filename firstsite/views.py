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


def SearchingAlgos(request):
    return HttpResponse("Searching Algorithms")


def SortingAlgos(request):
    return HttpResponse("Sorting Algorithms")


def GreedyAlgos(request):
    return HttpResponse("Greedy Algorithms")


def DynamicProgramming(request):
    return HttpResponse("Dynamic programming")


def PatternSearchingAlgos(request):
    return HttpResponse("Pattern Searching Algorithms")


def Backtracking(request):
    return HttpResponse("Back Tracking Algorithms")


def DivideAndConquer(request):
    return HttpResponse("Divide and Conquer Problems")


def GeometricAlgos(request):
    return HttpResponse("Geometric Algorithms")


def MathematicalAlgos(request):
    return HttpResponse("Mathematical Algorithms")


def BitAlgos(request):
    return HttpResponse("Bit Algorithms")

def GraphAlgos(request):
    return HttpResponse("Graph Algorithms")


def RandomizedAlgos(request):
    return HttpResponse("Randomized Algorithms")


def BranchAndBound(request):
    return HttpResponse("Branch and Bound problems")





