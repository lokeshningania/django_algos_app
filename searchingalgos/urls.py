from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "Search") ,
    path("linear",views.linearsearch , name ="linearsearch")
]