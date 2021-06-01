from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre_especialidad = models.TextField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre_especialidad

class Medico(models.Model):
    nombre_medico = models.TextField()
    especialidad = models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre_medico
    

TIPO_PREVISION = (
    ('Fonasa', 'Fonasa'),
    ('Isapre', 'Isapre'),
    ('Ninguna', 'Ninguna'),
)


class CitaMedica(models.Model):
    run= models.IntegerField(primary_key=True)
    nombre_paciente = models.TextField()
    tipo_prevision = models.CharField(max_length=50, choices=TIPO_PREVISION)
    medico = models.ForeignKey(Medico, related_name='medico', null=True, blank=True, on_delete=models.CASCADE)
    fecha_cita =  models.DateField()
    hora_cita = models.TimeField(blank=True, null=True)
    email = models.EmailField(max_length=70,blank=True, null= True)
    especialidad = models.ForeignKey(Especialidad, related_name='especialidad', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_paciente



