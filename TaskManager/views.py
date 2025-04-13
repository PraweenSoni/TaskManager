from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse('<h1>Welcome to Task Manager webapp</h1>')