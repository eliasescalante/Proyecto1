from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *


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
def cursoFormulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder\index.html")
    else:
        miFormulario=CursoFormulario()
    return render(request, "AppCoder\cursoFormulario.html", {"miFormulario":miFormulario})
def profesorFormulario(request):

    if request.method =='POST':

        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],
                        email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()

            return render(request, "AppCoder\index.html")
    else:
        miFormulario = ProfesorFormulario()
    return render(request,"AppCoder\profesorFormulario.html",{"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request, r"AppCoder\busquedaCamada.html")
def buscar(request):
   
    # return HttpResponse(respuesta)
    if request.GET["camada"]:
         # respuesta = f"Estoy buscando la camada nro : {request.GET['camada']}"
         camada = request.GET['camada']
         cursos = Curso.objects.filter(camada__icontains=camada)

         return render(request, r"AppCoder\resultadosBusqueda.html",{"cursos":cursos,"camada":camada})
    else:
        respuesta = "no enviaste datos"
    
    return HttpResponse(respuesta)
def imprimir(request):

    cursos = Curso.objects.all()
    
    context = {
        'cursos': cursos
    }
    return render(request, r"AppCoder\imprimirBase.html",context)
def leerProfesores(request):

    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}

    return render(request, "AppCoder\leerProfesores.html", contexto)
def eliminarProfesor(request,profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}

    return render(request, "AppCoder\leerProfesores.html",contexto)
def editarProfesor(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            return render(request, "AppCoder\index.html")
    else:
        # miFormulario = ProfesorFormulario()
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido,
                                            'email':profesor.email,'profesion':profesor.profesion})

    return render(request,"AppCoder\editarProfesores.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})


