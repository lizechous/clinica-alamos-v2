
from django import forms
from .models import CitaMedica, Medico

class CitaMedicaForm(forms.ModelForm): 
    class Meta:  
        model = CitaMedica
        fields = ['run', 'nombre_paciente', 'nombre_medico', 'especialidad', 'fecha_cita', 'hora_cita'
                  , 'email', 'precio', 'tipo_prevision'] 

        labels = {
            'run': 'Run',
            'nombre_paciente': 'Nombre paciente',
             
            'nombre_medico': 'Nombre medico',
            'especialidad': 'Especialidad',
            'fecha_cita': 'Fecha Cita',
            'hora_cita': 'Hora Cita',
            'email' : 'Email',
            'precio' : 'Precio',
            'tipo_prevision': 'Prevision',
        }
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_paciente': forms.TextInput(attrs={'class': 'form-control'}),
            
            'nombre_medico': forms.Select(choices="Medico", attrs={'class':'form-control'}),
            'especialidad': forms.Select(choices="TIPO_ESPECIALIDAD", attrs={'class':'form-control'}),
            'fecha_cita' : forms.TextInput(attrs={'class': 'form-control'}),
            'hora_cita' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_prevision': forms.Select(choices="TIPO_PREVISION", attrs={'class':'form-control'}),
            
        }