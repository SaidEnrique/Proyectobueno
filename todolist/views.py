from django.shortcuts import render , redirect
from .models import Tarea

def home(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect("home") 
    Tareas = Tarea.objects.all()
    return render(request, 'index.html', {'Tareas': Tareas})
