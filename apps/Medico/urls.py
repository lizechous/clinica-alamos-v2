from django.urls import path, include
from . import views

urlpatterns = [

    # listar las citas 
    path('listarCitas', views.listar_citas, name="listar_citas"),
]

