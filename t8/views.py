from django.shortcuts import render

def a(request):
	print("hi")
	return render(request, 't8/a.html')

def b(request):
	return render(request, 't8/b.html')

def c(request):
	return render(request, 't8/c.html')

def d(request):
	return render(request, 't8/d.html')

def e(request):
	return render(request, 't8/e.html')

def f(request):
	return render(request, 't8/f.html')

def g(request):
	return render(request, 't8/g.html')

def h(request):
	return render(request, 't8/h.html')

def index(request): 
	return render(request, "t8/index.html")
