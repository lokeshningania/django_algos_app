from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "backtrack") ,
    path("first",views.first , name ="first")
]