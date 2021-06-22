from django.contrib import admin
from .models import Secretaria, Medico, Paciente, Dueno
# Register your models here.
admin.site.register(Secretaria)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Dueno)