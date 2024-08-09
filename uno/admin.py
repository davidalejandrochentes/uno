from django.contrib import admin
from .models import Empleo, Comentario, Calificación, Trabajador

admin.site.register(Empleo)
admin.site.register(Trabajador)
admin.site.register(Comentario)
admin.site.register(Calificación)