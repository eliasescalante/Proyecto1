from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse('vista de inicio')

def cursos(request):
    return HttpResponse('vista cursos')

def profesores(request):
    return HttpResponse('vista profesores')

def estudiantes(request):
    return HttpResponse("Vista Estudiante")

def entregables(request):
    return HttpResponse("Vista Entregable")