# admisiones/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admision_view, name='admision'),  
]