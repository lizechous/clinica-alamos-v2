from django.shortcuts import render
from .models import CitaMedica
from .forms import CitaMedicaForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.db import connection
from .models import Especialidad, Medico
import json
from apps.Cuenta.decorators import unauthenticated_user, allowed_users, check_group
# Create your views here.

class Lista_citas_secretaria(ListView):
    model = CitaMedica
    template_name = 'Secretaria/lista_citas.html'


class Lista_medicos_pagos(ListView):
    model = CitaMedica
    template_name = 'Secretaria/lista_medicos_pagos.html'

# CREAR CITA
class Agregar_cita(CreateView): 
    #CitaMedica.objects.create(name='test')
    model = CitaMedica 
    form_class = CitaMedicaForm
    template_name = 'Secretaria/hora_form.html' 
    success_url = reverse_lazy('agregar_cita_secretaria')
    
# MODIFICAR CITA 
class Modificar_cita(UpdateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'Secretaria/hora_form.html'
    # success_url = reverse_lazy('agregar_cita')   
    success_url = reverse_lazy('lista_citas_secretaria') 

# ELIMINAR CITA 
# class Eliminar_cita(DeleteView):
#     model = CitaMedica
#     template_name = 'Secretaria/eliminar_cita.html'
#     success_url = reverse_lazy('lista_citas')

def eliminar_cita(request):
    run_cita = request.GET.get('run_cita', None)
    CitaMedica.objects.filter(run=run_cita).delete()
    return JsonResponse("{respuesta: ok}", safe=False)

def get_especialidades(request):
    id_especialidad = request.GET.get('id_especialidad', None)
    medicos = Medico.objects.filter(especialidad_id=id_especialidad)
    return JsonResponse(serializers.serialize('json', list(medicos)), safe=False)

def get_horas_no_disponibles(request):
    fecha_cita = request.GET.get('fecha_cita', None)
    rut_medico = request.GET.get('rut_medico', None)
    query = "select strftime('%H:%M', hora_cita) as 'hora_desde', strftime('%H:%M', time(hora_cita,'+45 minutes')) as 'hora_hasta' from Secretaria_citamedica where fecha_cita = '"+fecha_cita+"' and medico_id='"+rut_medico+"' order by hora_cita asc;"
    with connection.cursor() as cursor:
        cursor.execute(query)
        return JsonResponse(json.dumps(cursor.fetchall()), safe=False)

#----------------- PAGOS -------------------------------------------
# class Lista_medicos_pagos(ListView):
    # model = CitaMedica
    # template_name = 'HoraMedica/lista_medicos_pagos.html'


# FILTRO: BUSCAR MEDICO POR RUN
# TRAE LOS RESULTADOS DE LA BUSQUEDA
# class SearchResultsView(ListView):
#     model =CitaMedica
#     template_name = 'HoraMedica/search_results.html'
    
#     # def get_queryset(self): 
#     #     query = self.request.GET.get('q')
#     #     object_list = CitaMedica.objects.filter(
#     #         Q(medico__run_medico__icontains=query) )
        
#     #     return object_list

#     def get_queryset(self): 
#         # fecha = CitaMedica.fecha_cita.strftime('%m')
#         query = self.request.GET.get('q')
#         # object_list = CitaMedica.objects.filter(
#             # Q(fecha_cita__month=query) ).filter(Q(medico__run_medico__iconstains=query))
#         object_list= CitaMedica.objects.exclude(Q(medico__run_medico__iconstains=query,fecha_cita = date.month))

#         return object_list  

# def lista_medicos_pagos(request):
#     lista= CitaMedica.objects.all()
    # info que irá por get desde la caja de texto. Ej: run-medico es la caja d texto donde se ingresara eñ rut para ser buscado
    # run_medico= request.GET.get('run-medico')
    # fecha_cita= request.GET.get('fecha-cita')

    # if 'btn-buscar' in request.GET:
    #    if run_medico: 
    #        lista= CitaMedica.objects.filter(medico__run_medico__icontains=run_medico)
    #    if fecha_cita:
    #        lista= CitaMedica.objects.filter(fecha_cita__month=fecha_cita)
        #    lista= CitaMedica.objects.filter(fecha_cita__month=fecha_cita)
    #    if fecha_cita:
    #        lista= CitaMedica.objects.filter(fecha_cita__month=fecha_cita)
    # elif 'btn-buscar_fecha_cita' in request.GET:
    #     if fecha_cita:
    #         lista= CitaMedica.objects.filter(fecha_cita__month=fecha_cita)
      
    # data = {
    #     'object_list': lista
    # }
    # return render(request, 'Secretaria/lista_medicos_pagos.html', data)


#_---------------------------------------
def lista_medicos_pagos(request):
    lista= CitaMedica.objects.all()
    # info que irá por get desde la caja de texto. Ej: run-medico es la caja d texto donde se ingresara eñ rut para ser buscado
    run_medico= request.GET.get('run-medico')
    fecha_cita= request.GET.get('fecha-cita')

    if 'btn-buscar' in request.GET:
       if run_medico and fecha_cita: 
           lista= CitaMedica.objects.filter(medico__run_medico__icontains=run_medico).filter(fecha_cita__month=fecha_cita)
        #    lista= CitaMedica.objects.filter(fecha_cita__month=fecha_cita)
    #    if fecha_cita:
    #        lista= CitaMedica.objects.filter(fecha_cita__month=fecha_cita)
    # elif 'btn-buscar_fecha_cita' in request.GET:
    #     if fecha_cita:
    #         lista= CitaMedica.objects.filter(fecha_cita__month=fecha_cita)
      
    data = {
        'object_list': lista
    }
    return render(request, 'Secretaria/lista_medicos_pagos.html', data)