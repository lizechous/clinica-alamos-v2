
from django import forms
from .models import CitaMedica
class CitaMedicaForm(forms.ModelForm): 
    class Meta:  
        model = CitaMedica
        fields = ['run', 'nombre_paciente','tipo_prevision', 'especialidad', 'medico', 'fecha_cita', 'hora_cita'
                  , 'email'] 

        labels = {
            'run': 'Run',
            'nombre_paciente': 'Nombre paciente',
            'tipo_prevision': 'Prevision',
            'especialidad': 'Especialidad',
            'medico': 'Nombre medico',
            'fecha_cita': 'Fecha Cita',
            'hora_cita': 'Hora Cita',
            'email' : 'Email',
        }
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control', 'maxlength' : '12', 'onkeydown' : 'return soloTeclasRut(this)'}), 
            'nombre_paciente': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_prevision': forms.Select(attrs={'class':'form-control'}),
            'especialidad': forms.Select(attrs={'class':'form-control'}),
            'medico': forms.Select(attrs={'class':'form-control', 'disabled' : 'disabled'}),
            'fecha_cita' : forms.TextInput(attrs={'class': 'form-control', 'readonly' : 'readonly'}),
            'hora_cita' : forms.TextInput(attrs={'class': 'timepicker'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}), 
        }