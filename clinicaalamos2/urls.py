from django.contrib import admin
from django.urls import path, include
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from apps.Cuenta import views as user_views
from apps.Secretaria import views as secretaria_views
from apps.Medico import views as medico_views
from apps.Paciente import views as paciente_views
from django.conf.urls import url
from apps.Cuenta.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url('especialidad/get_especialidades/$', secretaria_views.get_especialidades, name='get_especialidades'),
    url('especialidad/get_horas_no_disponibles/$', secretaria_views.get_horas_no_disponibles, name='get_horas_no_disponibles'),
    url('especialidad/eliminar_cita/$', secretaria_views.eliminar_cita, name='eliminar_cita'),

    path('register/', user_views.registerPage, name="register"),
    path('login/', user_views.loginPage, name="login"),
    path('logout/', user_views.logoutUser, name="logout"),
    path('user/', user_views.logoutUser, name="user-page"),
    path('secretaria/agregar_cita', secretaria_views.Agregar_cita.as_view(), name="agregar_cita_secretaria"),
    path('secretaria/editar_cita/<str:pk>', secretaria_views.Modificar_cita.as_view(), name='editar_cita'),
    # path('secretaria/eliminar_cita/<str:pk>', medico_views.Eliminar_cita.as_view(), name='eliminar_cita'),
    path('medico/lista_citas', medico_views.Lista_citas, name="lista_citas"),
    path('paciente/agregar_cita', paciente_views.Agregar_cita.as_view(), name="agregar_cita_paciente"), 
    path('secretaria/lista_pagos/', login_required(login_url='login')(secretaria_views.lista_medicos_pagos) , name="lista_medicos_pagos"), 
]

