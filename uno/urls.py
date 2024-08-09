from django.urls import path
from . import views

urlpatterns = [
    path('', views.empleo, name="empleo"),
    path('trabajador/<int:id>', views.trabajador, name="trabajador")
]
