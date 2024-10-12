from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
     path("",views.index,name="Home"),
    path("Teampage",views.Teampage,name="Teampage"),
   
    path("achievements",views.achievements,name="achievements"),
    path("projectstatus",views.ProjectStatus,name="ProjectStatus"),
    path("contact",views.contact,name="conatct"),


]