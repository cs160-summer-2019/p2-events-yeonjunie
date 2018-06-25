from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a/',views.a, name='a'),
    path('b/',views.b, name='b'),
    path('c/',views.c, name='c'),
    path('d/',views.d, name='d'),
    path('e/',views.e, name='e'),
    path('f/',views.f, name='f')
]