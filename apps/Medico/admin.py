from django.contrib import admin
from .models import CitaMedica, Medico

# Register your models here.
admin.site.register(Medico)
admin.site.register(CitaMedica)