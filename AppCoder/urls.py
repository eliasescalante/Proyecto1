from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('cursos', views.Cursos, name="Cursos"),
    path('profesores', views.profesores,name="Profesores"),
    path('estudiantes',views.estudiantes,name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario',views.cursoFormulario,name="CursoFormulario"),
    path('profesorFormulario',views.profesorFormulario,name="ProfesorFormulario"),
    path('busquedaCamada', views.busquedaCamada,name="BusquedaCamada"),
    path('buscar', views.buscar),
    path('imprimir', views.imprimir,name="Imprimir"),
    path('leerProfesores', views.leerProfesores,name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor,name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor,name="EditarProfesor"),
    path('login', views.login_request,name= 'Login'),
    path('register', views.register,name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'),name='Logout'),
]

urlpatterns += [
    path('clases/lista/', views.CursoListView.as_view(),name='List'),
    path('clases/detalle/<int:pk>', views.CursoDetalle.as_view(), name='Detail'),
    path('clases/nuevo/', views.CursoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views.CursoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views.CursoDeleteView.as_view(),name='Delete')
]