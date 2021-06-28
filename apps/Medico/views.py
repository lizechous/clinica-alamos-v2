# from apps.Medico.models import CitaMedica
from apps.Medico.forms import CitaMedicaForm
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Especialidad, Medico
from apps.Secretaria.models import CitaMedica
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.db import connection
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.Cuenta.decorators import unauthenticated_user, allowed_users, check_group

from datetime import date
# Create your views here.




@login_required(login_url='login')
@allowed_users(allowed_roles=['medico'])
def Lista_citas(request):
    rutUsuario = request.user.usuario.rut
    nombre_medico= request.GET.get('nombre-medico')
    lista= CitaMedica.objects.filter(medico__run_medico__contains=rutUsuario)

    if 'btn-buscarMedicos' in request.GET:
        if nombre_medico: 
        #    fk: tabla medico, atributo nombre_medico = a nombre_medico del get
            lista= CitaMedica.objects.filter(medico__nombre_medico__icontains=nombre_medico)
    data = {
        'object_list': lista
    }
    return render(request, 'Medico/lista_citas.html', data)

def get_especialidades(request):
    id_especialidad = request.GET.get('id_especialidad', None)
    medicos = Medico.objects.filter(especialidad_id=id_especialidad)
    return JsonResponse(serializers.serialize('json', list(medicos)), safe=False)

def get_horas_no_disponibles(request):
    fecha_cita = request.GET.get('fecha_cita', None)
    with connection.cursor() as cursor:
        cursor.execute("select hora_cita as 'hora_desde', time(hora_cita,'+45 minutes')"+
    " as 'hora_hasta' from Secretaria_citamedica where fecha_cita = "+fecha_cita+" order by hora_cita asc;")
        return JsonResponse(serializers.serialize('json', list(cursor.fetchall())), safe=False)

def lista_medicos_citas(request):
    lista= CitaMedica.objects.all()
    # info que irá por get desde la caja de texto. Ej: run-medico es la caja d texto donde se ingresara eñ rut para ser buscado
    run_medico= request.GET.get('run-medico')
    fecha_cita= request.GET.get('fecha-cita')

    if 'btn-buscar' in request.GET:
       if run_medico and fecha_cita: 
           lista= CitaMedica.objects.filter(medico__run_medico__icontains=run_medico).filter(fecha_cita__month=fecha_cita)
      
    data = {
        'object_list': lista
    }
    return render(request, 'Medico/lista_citas.html', data)

# # MODIFICAR CITA 
# class Modificar_cita(UpdateView):
#     model = CitaMedica
#     form_class = CitaMedicaForm
#     template_name = 'Secretaria/hora_form.html'
#     # success_url = reverse_lazy('agregar_cita')   
#     success_url = reverse_lazy('lista_medicos_pagos') 

# # ELIMINAR CITA 
# class Eliminar_cita(DeleteView):
#     model = CitaMedica
#     template_name = 'Secretaria/eliminar_cita.html'
#     success_url = reverse_lazy('lista_citas')