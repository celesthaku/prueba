from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    return render(request, "index.html")

def gallery(request):
    return render(request, "/pages/gallery.html")
