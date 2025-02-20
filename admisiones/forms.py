from django import forms
from .models import FormularioAdmision

class FormularioAdmisionForm(forms.ModelForm):
    class Meta:
        model = FormularioAdmision
        fields = ['primer_nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno', 
                  'tipo_documento', 'numero_documento', 'fecha_nacimiento', 'nacionalidad', 'sexo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(choices=[('M', 'Masculino'), ('F', 'Femenino')]),
            'tipo_documento': forms.Select(choices=[('DNI', 'DNI'), ('CARNET', 'Carnet de Extranjería')]),
            'nacionalidad': forms.Select(choices=[('PE', 'Perú'), ('VE', 'Venezuela')]), 
        }
