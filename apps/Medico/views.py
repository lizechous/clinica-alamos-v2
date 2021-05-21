from apps.Medico.models import CitaMedica
from django.shortcuts import render

# Create your views here.
def listar_citas(request):
    citas = CitaMedica.objects.all()
    return render(request, "Medico/listar_citas.html", {'citas': citas})
