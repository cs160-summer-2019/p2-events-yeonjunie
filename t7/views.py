from django.shortcuts import render


def a(request):
	return render(request, 't7/a.html')

def b(request):
	return render(request, 't7/b.html')

def index(request): 
	return render(request, "t7/index.html")
