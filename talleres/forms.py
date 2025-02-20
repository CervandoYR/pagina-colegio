from django import forms
from .models import InscripcionTaller  
class FormularioTalleresForm(forms.ModelForm):
    class Meta:
        model = InscripcionTaller
        fields = ['nombre', 'apellido', 'correo', 'numero', 'apoderado', 'grado', 'seccion', 'taller', 'horario']

    grado = forms.ChoiceField(choices=InscripcionTaller.GRADO_CHOICES, required=True)
    seccion = forms.ChoiceField(choices=InscripcionTaller.SECCION_CHOICES, required=True)
