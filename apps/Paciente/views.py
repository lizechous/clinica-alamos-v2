from django.shortcuts import render
from apps.Secretaria.models import CitaMedica
from apps.Secretaria.forms import CitaMedicaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class Agregar_cita(CreateView): 
    #CitaMedica.objects.create(name='test')
    model = CitaMedica 
    form_class = CitaMedicaForm
    template_name = 'Paciente/hora_form.html' 
    success_url = reverse_lazy('agregar_cita_paciente')