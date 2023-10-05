from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



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

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            con = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=con)

            if user is not None:
                login(request,user)

                return render(request,"AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()

    return render (request,"AppCoder/login.html", {'form':form})

def register(request):

    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html", {"mensaje":"Usuario creado..."})
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    
    return render(request, "AppCoder/registro.html", {"form":form})

#########################################################################################################################################



class CursoListView(ListView):
    model = Curso
    template_name = "AppCoder/lista.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreateView(CreateView):
    model = Curso
    template_name = "AppCoder/curso_form.html"
    success_url = reverse_lazy("List")
    fields = ['nombre', 'camada']

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "AppCoder/curso_edit.html"
    success_url = "/AppCoder/lista/"
    fields = ['nombre', 'camada']

class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("List")
    template_name = "AppCoder/curso_confirm_delete.html"
