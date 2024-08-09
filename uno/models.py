from django.db import models
from datetime import date
import uuid

# Create your models here.
class Empleo(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Calificación(models.Model):
    estrellas = models.CharField(max_length=1, null=False, blank=False)

    def __str__(self):
        return self.estrellas
    
class Trabajador(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    dirección = models.TextField(max_length=100, default="", null=False, blank=False)
    ci = models.IntegerField(max_length=11, blank=False, null=False)
    empresa = models.CharField(max_length=30, blank=False, null=False)
    teléfono1 = models.CharField(max_length=15, blank=False, null=False)
    teléfono2 = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    imagen = models.ImageField(upload_to="empleados/imagen", null=False, blank=False)
    domicilio = models.BooleanField(default=True, blank=False, null=False)
    descripción = models.TextField(max_length=400, null=False, blank=False, default="")
    fecha_alta = models.DateField(default=date.today, blank=False, null=False)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    calificación = models.ForeignKey(Calificación, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lon = models.DecimalField(max_digits=10, decimal_places=7)
    token = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self._generate_token()
        super().save(*args, **kwargs)
    def _generate_token(self):
        return get_random_string(length=30)

    def __str__(self):
        txt = "Nombre: {}, Apellido: {}, CI: {}"
        return txt.format(self.nombre, self.apellido, self.ci)

class Comentario(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False, default="")
    comentario = models.TextField(max_length=400, blank=False, null=False)
    calificación = models.ForeignKey(Calificación, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return self.comentario