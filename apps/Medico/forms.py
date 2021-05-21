from django import forms
from .models import CitaMedica

class CitaMedicaForm(forms.ModelForm): 
    class Meta:  
        model = CitaMedica
        fields = ['run', 'nombre_paciente', 'tipo_prevision', 'medico', 'especialidad', 'fecha_cita', 'hora_cita'] 

        labels = {
            'run': 'Run',
            'nombre_paciente': 'Nombre paciente',
            'tipo_prevision': 'Prevision', 
            'medico': 'Nombre medico',
            'especialidad': 'Especialidad',
            'fecha_cita': 'Fecha Cita',
            'hora_cita': 'Hora Cita',
        }
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_paciente': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_prevision': forms.Select(choices="TIPO_PREVISION", attrs={'class':'form-control'}),
            'medico': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(choices="TIPO_ESPECIALIDAD", attrs={'class':'form-control'}),
            'fecha_cita' : forms.TextInput(attrs={'class': 'form-control'}),
            'hora_cita' : forms.TextInput(attrs={'class': 'form-control'}),
        }