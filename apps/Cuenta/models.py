from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from apps.Medico.models import Medico

TIPO_USUARIO = (
    ('paciente', 'Paciente'),
    ('secretaria', 'Secretaria'),
    ('medico', 'Médico'),
    ('dueno', 'Dueño')
)

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    rut = models.CharField(max_length=12, null=True)
    tipo = models.CharField(max_length=50, choices=TIPO_USUARIO)

    def __str__(self):
        return self.name


# class MedicoUser(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     medico = models.ForeignKey(Medico, null=True, blank=True, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
    
#     def __str__(self):
#         return self.name

# class Paciente(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
    
#     def __str__(self):
#         return self.name

# class Dueno(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
    
#     def __str__(self):
#         return self.name
