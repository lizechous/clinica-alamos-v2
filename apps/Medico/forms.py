
from django import forms
from .models import CitaMedica, Medico

class CitaMedicaForm(forms.ModelForm): 
    class Meta:  
        model = CitaMedica
        fields = ['run', 'nombre_paciente','tipo_prevision', 'especialidad', 'nombre_medico', 'fecha_cita', 'hora_cita'
                  , 'email'] 

        labels = {
            'run': 'Run',
            'nombre_paciente': 'Nombre paciente',
            'tipo_prevision': 'Prevision',
            'especialidad': 'Especialidad',
            'nombre_medico': 'Nombre medico',
            'fecha_cita': 'Fecha Cita',
            'hora_cita': 'Hora Cita',
            'email' : 'Email',
        }
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_paciente': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_prevision': forms.Select(choices="TIPO_PREVISION", attrs={'class':'form-control'}),
            'especialidad': forms.Select(choices="Especialidad", attrs={'class':'form-control'}),
            'nombre_medico': forms.Select(choices="Medico", attrs={'class':'form-control'}),
            'fecha_cita' : forms.TextInput(attrs={'class': 'form-control'}),
            'hora_cita' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}), 
        }