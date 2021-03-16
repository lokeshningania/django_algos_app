from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "greedy") ,
    path("first",views.first , name ="first")
]