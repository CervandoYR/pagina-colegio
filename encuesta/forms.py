from django import forms
from .models import Encuesta

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'apellido', 'correo', 'calificacion_atencion', 'escuchado', 'recomendacion', 'calificacion_instalaciones', 'experiencia_general']


    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Encuesta.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya ha sido registrado.")
        return correo
