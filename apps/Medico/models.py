from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre_especialidad = models.TextField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre_especialidad

class Medico(models.Model):
    run_medico = models.TextField(primary_key=True)
    nombre_medico = models.TextField()
    especialidad = models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre_medico
    

TIPO_PREVISION = (
    ('Fonasa', 'Fonasa'),
    ('Isapre', 'Isapre'),
    ('Ninguna', 'Ninguna'),
)






