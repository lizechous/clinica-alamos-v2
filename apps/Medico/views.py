# from apps.Medico.models import CitaMedica
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import CitaMedica, Medico
from .forms import CitaMedicaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q 

# Create your views here.

# CREAR CITA
class Agregar_cita(CreateView): 
    model = CitaMedica 
    form_class = CitaMedicaForm
    template_name = 'HoraMedica/hora_form.html' 
    success_url = reverse_lazy("agregar_cita")


# LISTADO DE CITAS AGENDADAS
# def listar_citas(request):
#     citas = CitaMedica.objects.all()
#     return render(request, "Medico/listar_citas.html", {'citas': citas})

class Lista_citas(ListView):
    model = CitaMedica
    template_name = 'HoraMedica/lista_citas.html'
    

# MODIFICAR CITA 
class Modificar_cita(UpdateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'HoraMedica/hora_form.html'
    # success_url = reverse_lazy('agregar_cita')   
    success_url = reverse_lazy('lista_citas') 

# ELIMINAR CITA 
class Eliminar_cita(DeleteView):
    model = CitaMedica
    template_name = 'HoraMedica/eliminar_cita.html'
    success_url = reverse_lazy('lista_citas')

def get_especialidades(request):
    id_especialidad = request.GET.get('id_especialidad', None)
    medicos = Medico.objects.raw('SELECT * FROM Medico_medico where especialidad_id='+id_especialidad)
    return JsonResponse(serializers.serialize('json', medicos), safe = False)

#----------------- PAGOS -------------------------------------------
class Lista_medicos_pagos(ListView):
    model = CitaMedica
    template_name = 'HoraMedica/lista_medicos_pagos.html'


