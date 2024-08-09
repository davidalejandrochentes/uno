from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Empleo, Comentario, Trabajador


def empleo(request):
    empleos = Empleo.objects.filter(nombre__icontains=request.GET.get('search', ''))
    context = {
        'empleos': empleos,
    }
    return render(request, 'uno/empleos.html', context)

def trabajador(request, id):
    trabajadores = Trabajador.objects.filter(empleo = id)
    context = {
        'trabajadores': trabajadores,
    }
    return render(request, 'uno/trabajadores.html', context)