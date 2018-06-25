from django.shortcuts import render

def a(request):
	print("hi")
	return render(request, 't6/a.html')

def b(request):
	return render(request, 't6/b.html')

def c(request):
	return render(request, 't6/c.html')

def d(request):
	return render(request, 't6/d.html')

def e(request):
	return render(request, 't6/e.html')

def f(request):
	return render(request, 't6/f.html')

def index(request): 
	return render(request, "t6/index.html")
