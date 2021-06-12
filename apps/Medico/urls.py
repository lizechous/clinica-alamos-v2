from django.urls import path, include
from django.conf.urls import url
from . import views
from apps.Medico.views import Agregar_cita, Lista_citas, Modificar_cita, Eliminar_cita, SearchResultsView
# from .views import views mantenedor

urlpatterns = [

#------------ HORAS MEDICAS ---------------
    # Agregar cita medica
    path('horaMedica/agregar_cita', views.Agregar_cita.as_view(), name="agregar_cita"),
    #url('horaMedica/agregar_cita', views.get_especialidades, name='get_especialidades'),     

    # Listar las citas 
    # path('listarCitas', views.listar_citas, name="listar_citas"),
    path('horaMedica/lista_citas', views.Lista_citas.as_view() , name="lista_citas"), 
    
    # Modificar cita 
    path('horaMedica/editar_cita/<str:pk>', views.Modificar_cita.as_view(), name='editar_cita'),

    # Eliminar cita
    path('horaMedica/eliminar_cita/<str:pk>', views.Eliminar_cita.as_view(), name='eliminar_cita'),

    url('especialidad/get_especialidades/$', views.get_especialidades, name='get_especialidades'),
    
    # -----------PAGOS-------------------------
    # trae los pagos de todos los medicos 
    path('horaMedica/lista_pagos', views.Lista_medicos_pagos.as_view(), name='lista_medicos_pagos'),
    
    # FILTRO: BUSCAR MEDICO
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
