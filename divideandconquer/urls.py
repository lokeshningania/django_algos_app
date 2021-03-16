from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "divideandconquer") ,
    path("first",views.first , name ="first")
]