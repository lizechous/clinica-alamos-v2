from django.shortcuts import render
from apps.Secretaria.models import CitaMedica
from apps.Secretaria.forms import CitaMedicaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db import connection
from django.http import JsonResponse
import json

# Create your views here.
class Agregar_cita(CreateView): 
    #CitaMedica.objects.create(name='test')
    model = CitaMedica 
    form_class = CitaMedicaForm
    template_name = 'Paciente/hora_form.html' 
    success_url = reverse_lazy('agregar_cita_paciente')

def get_horas_no_disponibles(request):
    fecha_cita = request.GET.get('fecha_cita', None)
    rut_medico = request.GET.get('rut_medico', None)
    query = "select strftime('%H:%M', hora_cita) as 'hora_desde', strftime('%H:%M', time(hora_cita,'+45 minutes')) as 'hora_hasta' from Secretaria_citamedica where fecha_cita = '"+fecha_cita+"' and medico_id='"+rut_medico+"' order by hora_cita asc;"
    with connection.cursor() as cursor:
        cursor.execute(query)
        return JsonResponse(json.dumps(cursor.fetchall()), safe=False)