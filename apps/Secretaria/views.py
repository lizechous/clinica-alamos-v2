from django.shortcuts import render
from .models import CitaMedica
from .forms import CitaMedicaForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q 
from django.db.models import Sum
from apps.Cuenta.decorators import unauthenticated_user, allowed_users, check_group
# Create your views here.


class Lista_medicos_pagos(ListView):
    model = CitaMedica
    template_name = 'Secretaria/lista_medicos_pagos.html'

# CREAR CITA
class Agregar_cita(CreateView): 
    #CitaMedica.objects.create(name='test')
    model = CitaMedica 
    form_class = CitaMedicaForm
    template_name = 'Secretaria/hora_form.html' 
    success_url = reverse_lazy('agregar_cita')
    
# MODIFICAR CITA 
class Modificar_cita(UpdateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'Secretaria/hora_form.html'
    # success_url = reverse_lazy('agregar_cita')   
    success_url = reverse_lazy('lista_citas') 

# ELIMINAR CITA 
class Eliminar_cita(DeleteView):
    model = CitaMedica
    template_name = 'Secretaria/eliminar_cita.html'
    success_url = reverse_lazy('lista_citas')


def get_especialidades(request):
    id_especialidad = request.GET.get('id_especialidad', None)
    medicos = Medico.objects.filter(especialidad_id=id_especialidad)
    return JsonResponse(serializers.serialize('json', list(medicos)), safe=False)


