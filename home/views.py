from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
from datetime import datetime


def index(request) :
    return render(request,'home.html')

def Teampage(request):
    return render(request,'teampage.html')

def achievements(request):
    return render(request,'achievements.html')

def ProjectStatus(request):
    return render(request,'ProjectStatus.html')
def contact(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        namecompany=request.POST.get('namecompany')
        position=request.POST.get('position')
        
        contact=Contact(Name=Name,Email=Email,Phone=Phone,desc=desc,namecompany=namecompany,position=position)
        contact.save()
        messages.success(request, "The message has been delivered!")
    return render(request,'contact.html')

# Create your views here.
