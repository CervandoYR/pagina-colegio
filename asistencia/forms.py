# asistencia/forms.py
from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['empleado', 'estado', 'fecha']

    def clean(self):
        cleaned_data = super().clean()
        empleado = cleaned_data.get('empleado')
        fecha = cleaned_data.get('fecha')

        if Asistencia.objects.filter(empleado=empleado, fecha=fecha).exists():
            raise forms.ValidationError(f'Asistencia ya registrada para {empleado} en esta fecha.')
        return cleaned_data
