from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Alumno
from .forms import LibroForm, AlumnoForm

# Create your views here.

def inicio(request):
    total_libros = Libro.objects.count()
    total_alumnos = Alumno.objects.count()
    return render(request,"inicio.html", {
        "total_libros": total_libros,
        "total_alumnos": total_alumnos
})
def lista_libros(request):
    libro = Libro.objects.all()
    return render(request,"lista_libros.html", {"libros": libro})
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request,"lista_alumnos.html", {"alumnos": alumnos})
