from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
# Create your views here.

def index(request):
    persons = Image.objects.order_by('-title')
    context = {'persons': persons}
    return render(request, "main/index.html", context=context)

def about(requset):
    persons = Image.objects.order_by('-title')
    context = {'persons': persons}
    return render(requset, "main/about.html", context=context)

def home(request):
    return redirect("http://localhost:8000/home/")

def service(request):
    return render(request, "main/service.html")

