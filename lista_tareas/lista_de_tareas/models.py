from django.db import models

class Tarea(models.Model):
    CATEGORIAS = (
        ('hogar', 'Hogar'),
        ('estudio', 'Estudio'),
        ('trabajo', 'Trabajo'),
    )
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='hogar')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo