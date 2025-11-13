from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=150)
    
    def __str__(self):
        return self.titulo  
