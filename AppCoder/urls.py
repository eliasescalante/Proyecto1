from django.urls import path
from AppCoder import views
from Proyecto1.views import *

urlpatterns = [
    
    path('curso/',curso),
    path('',views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores),
    path('estudiantes',views.estudiantes),
    path('entregables', views.entregables)
]