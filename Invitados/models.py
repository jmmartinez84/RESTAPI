from django.db import models

class Invitado(models.Model):
    telefono = models.CharField(max_length=15)
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)