# from apps.Medico.models import CitaMedica
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Especialidad, Medico
from apps.Secretaria.models import CitaMedica
from .forms import CitaMedicaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q 
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from apps.Cuenta.decorators import unauthenticated_user, allowed_users, check_group

# Create your views here.




@login_required(login_url='login')
@allowed_users(allowed_roles=['medico'])
def Lista_citas(request):
    lista= CitaMedica.objects.all()
    nombre_medico= request.GET.get('nombre-medico')

    if 'btn-buscarMedicos' in request.GET:
        if nombre_medico: 
        #    fk: tabla medico, atributo nombre_medico = a nombre_medico del get
            lista= CitaMedica.objects.filter(medico__nombre_medico__icontains=nombre_medico)
    data = {
        'object_list': lista
    }
    return render(request, 'Medico/lista_citas.html', data)
