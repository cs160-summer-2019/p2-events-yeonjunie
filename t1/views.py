from django.shortcuts import render
from django.http import HttpResponse


def a(request):
    return render(request, 't1/a.html')

def b(request):
    return render(request, 't1/b.html')

def index(request):
    return render(request, 't1/index.html')