# urls.py
from django.urls import path
from .views import inscripcion_talleres_view

urlpatterns = [
    path('inscripcion/', inscripcion_talleres_view, name='inscripcion_talleres'),
]
