from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "bitalgos") ,
    path("first",views.first , name ="first")
]