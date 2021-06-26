# from apps.Medico.models import CitaMedica
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import CitaMedica, Especialidad, Medico
from .forms import CitaMedicaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q 
from django.db.models import Sum

from datetime import date
# Create your views here.

# CREAR CITA
class Agregar_cita(CreateView): 
    #CitaMedica.objects.create(name='test')
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
    medicos = Medico.objects.filter(especialidad_id=id_especialidad)
    return JsonResponse(serializers.serialize('json', list(medicos)), safe=False)

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
    return render(request, 'HoraMedica/lista_medicos_pagos.html', data)