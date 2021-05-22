from django.urls import path, include
from . import views
from apps.Medico.views import Agregar_cita, Lista_citas, Modificar_cita

urlpatterns = [

#------------ HORAS MEDICAS ---------------
    # Agregar cita medica
     path('horaMedica/agregar_cita', views.Agregar_cita.as_view(), name="agregar_cita"),
     
    # Listar las citas 
    # path('listarCitas', views.listar_citas, name="listar_citas"),
    path('horaMedica/lista_citas', views.Lista_citas.as_view(), name='lista_citas'),
    
    # Modificar cita 
    path('horaMedica/editar_cita/<int:pk>', views.Modificar_cita.as_view(), name='editar_cita'),

]

