from django.shortcuts import render
from django.http import HttpResponse


def a(request):
    return render(request, 'a.html')

def b(request):
    return render(request, 'b.html')

def index(request):
    return render(request, 'index.html')
