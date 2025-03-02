from django.db import models
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    prioridad = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField(null=True, blank=True)
    completado = models.BooleanField(default=False)

class Meta:
    db_table = 'tasks'