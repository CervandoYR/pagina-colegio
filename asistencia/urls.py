# asistencia/urls.py
from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('registrar/', view = views.registrar_asistencia, name='registrar_asistencia'),
    path('lista_asistencias/', view = views.lista_asistencias, name='lista_asistencias'),
    
    
]
