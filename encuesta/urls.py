from django.urls import path
from .views import encuesta_view 

urlpatterns = [
    path('', encuesta_view, name='encuesta'),  
]
