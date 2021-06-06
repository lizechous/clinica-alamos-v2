from django.urls import path, include
from django.conf.urls import url
from . import views
from apps.Secretaria.views import Lista_medicos_pagos
from .views import views as secretaria_views

urlpatterns = [
    url('secretaria/especialidades/$', secretaria_views.get_especialidades, name='get_especialidades'),
]

