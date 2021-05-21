from django.urls import path, include
from . import views


urlpatterns = [

#------------ HORAS MEDICAS ---------------
    # agregar hora
     path('agregar_cita', views.Agregar_cita.as_view(), name="agregar_cita"),
    # listar las citas 
    path('listarCitas', views.listar_citas, name="listar_citas"),
]

