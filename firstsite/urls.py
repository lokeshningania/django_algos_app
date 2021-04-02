"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countdown' , views.countdown , name = 'countdown'),
    path('' , views.home , name = 'home'),
    path('algos', views.algos, name = 'algos'),
    path('submit' , views.submit , name = 'submit'),
    path('ds/' , include('datastructures.urls')),
    path('geometry/' , include('geometricalgos.urls')),
    path('maths/' , include('mathematicalalgos.urls')),
    path('backtrack/' , include('backtracking.urls')),
    path('bit/' , include('bitalgos.urls')),
    path('branchandbound/' , include('branchandbound.urls')),
    path('greedy/' , include('greedyalgos.urls')),
    path('sort/' , include('sortingalgos.urls')),
    path('search/' , include('searchingalgos.urls')),
    path('divcon/' , include('divideandconquer.urls')),
    path('pattern/' , include('patternsearchingalgos.urls')),
    path('dynamic/' , include('dynamicprogramming.urls')),
    path('randomised/' , include('randomizedalgos.urls')),
    path('graph/' , include('graphalgos.urls')),
]
