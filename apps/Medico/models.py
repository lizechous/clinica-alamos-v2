from django.db import models

# Create your models here.
TIPO_ESPECIALIDAD = (
    ('Cirugía', 'Cirugía'),
    ('Cardiología', 'Cardiología'),
    ('Odontología', 'Odontología'),
    ('Pediatría', 'Pediatría'),
    ('Ginecología', 'Ginecología'),
    ('Oftomología', 'Oftomología'),
)


class Medico(models.Model):
    nombre_medico = models.TextField()
    # nombre_medico = models.TextField(max_length=30)
    tipo_Especialidad = models.CharField(max_length=50, choices=TIPO_ESPECIALIDAD)


    def __str__(self):
        return self.nombre_medico
    

TIPO_PREVISION = (
    ('Fonasa', 'Fonasa'),
    ('Isapre', 'Isapre'),
    ('Ninguna', 'Ninguna'),
)


class CitaMedica(models.Model):
    run = models.IntegerField(primary_key=True)
    nombre_paciente = models.TextField()
    tipo_prevision = models.CharField(max_length=50, choices=TIPO_PREVISION)
    # medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    nombre_medico = models.TextField()
    especialidad = models.CharField(max_length=50, choices=TIPO_ESPECIALIDAD)
    fecha_cita =  models.DateField()
    hora_cita = models.TimeField(blank=True, null=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre_paciente

# , null=True -- hora
# , null= True, unique= True -- email
