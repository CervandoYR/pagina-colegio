from django.shortcuts import render
from asistencia.models import Asistencia
from django.db.models import Q

def dashboard(request):
    # Obtener las asistencias con filtros opcionales
    nombre_filtro = request.GET.get('nombre', '')
    estado_filtro = request.GET.get('estado', '')
    fecha_inicio_filtro = request.GET.get('fecha_inicio', '')
    fecha_fin_filtro = request.GET.get('fecha_fin', '')
    
    # Filtrar las asistencias basadas en los parámetros
    asistencias = Asistencia.objects.all()

    if nombre_filtro:
        asistencias = asistencias.filter(empleado__nombre__icontains=nombre_filtro)
    if estado_filtro:
        asistencias = asistencias.filter(estado=estado_filtro)
    if fecha_inicio_filtro:
        asistencias = asistencias.filter(fecha__gte=fecha_inicio_filtro)
    if fecha_fin_filtro:
        asistencias = asistencias.filter(fecha__lte=fecha_fin_filtro)

    # Calcular el número total de registros
    total_asistencias = asistencias.count()

    # Calcular el número de presentes y ausentes
    presentes = asistencias.filter(estado='Presente').count()
    ausentes = asistencias.filter(estado='Ausente').count()

    # Calcular los promedios
    promedio_presente = (presentes / total_asistencias) * 100 if total_asistencias > 0 else 0
    promedio_ausente = (ausentes / total_asistencias) * 100 if total_asistencias > 0 else 0

    return render(request, 'dashboard/dashboard.html', {
        'asistencias': asistencias,
        'promedio_presente': promedio_presente,
        'promedio_ausente': promedio_ausente,
    })
