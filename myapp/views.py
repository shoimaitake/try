from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def HomeView(request):
    return render(request, "myapp/home.html")

def ProfileView(request):
    return render(request, "myapp/profile.html")

def AddSlotView(request):
    return render(request, "myapp/add_slot.html")

def ReserveView(request):
    return render(request, "myapp/reserve.html")