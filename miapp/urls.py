from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio, name="inicio"),
    path("libros/", views.lista_libros, name="lista_libros"),
    path("alumnos/", views.lista_alumnos, name="lista_alumnos"), 

]