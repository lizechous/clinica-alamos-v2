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
    autor_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre_medico = models.TextField()
    tipo_Especialidad = models.CharField(max_length=50, choices=TIPO_ESPECIALIDAD)


    def __str__(self):
        return self.nombre_medico
    
