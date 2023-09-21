from django.http import HttpResponse
import datetime 
from django.template import Template, Context
from django.template import loader
from AppCoder.models import Curso

def saludo(request):
	return HttpResponse("hola django soy elias...")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple")

def diaDeHoy(request):
    dia = datetime.datetime.now() #obtenemos la fecha actual del sistema operativo
    documentoDeTexto = f"hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"

    return HttpResponse(documentoDeTexto)

def probandoTemplate(request):
    # miHtml = open(r"C:\Users\yuens\Desktop\Ninja\FACULTAD - CURSOS\Curso PY\CODERHOUSE\clase_17_django\Proyecto1\Proyecto1\plantillas\template1.html")
    # plantilla = Template(miHtml.read())
    # miHtml.close()
    # miContexto = Context()

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render({'nombre':"elias"})

    return HttpResponse(documento)

def probandoTemplate2(request):
    nombre = "Elias"
    apellido = "Escalante"
    listaDeNotas = [1,2,3,4,5]

    diccionario = {"nombre": nombre, "apellido":apellido, "notas":listaDeNotas}
    # miHtml = open(r"C:\Users\yuens\Desktop\Ninja\FACULTAD - CURSOS\Curso PY\CODERHOUSE\clase_17_django\Proyecto1\Proyecto1\plantillas\template2.html")
    # plantilla = Template(miHtml.read())
    # miHtml.close()
    # miContexto = Context(diccionario)

    plantilla = loader.get_template("template2.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def curso(self):
    curso = Curso(nombre="SQL", camada=27001)
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)

