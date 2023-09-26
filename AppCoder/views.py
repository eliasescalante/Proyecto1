from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request,"AppCoder\index.html")

def Cursos(request):
    return render(request,"AppCoder\cursos.html")

def profesores(request):
    return render(request,"AppCoder\profesores.html")

def estudiantes(request):
    return render(request,"AppCoder\estudiantes.html")

def entregables(request):
    return render(request,"AppCoder\entregables.html")