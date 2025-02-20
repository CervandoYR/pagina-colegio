from django.shortcuts import render, redirect
from .models import Asistencia
from marcacion.models import Empleado
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, localtime
from django.contrib import messages
from django.db import IntegrityError  # Para capturar errores de unicidad

@login_required(login_url='login')
def registrar_asistencia(request):
    today = now().date()  # Fecha actual
    empleados = Empleado.objects.all()
    se_registro_asistencia = False

    if request.method == 'POST':
        for empleado in empleados:
            estado = request.POST.get(f'empleado_{empleado.id}')
            if estado:
                # Verifica si ya existe una asistencia para este empleado hoy
                try:
                    Asistencia.objects.create(
                        empleado=empleado,
                        estado=estado,
                        fecha=today,
                        hora_marcado=localtime(now()).time().replace(microsecond=0)
                    )
                    se_registro_asistencia = True
                except IntegrityError:
                    messages.warning(request, f'La asistencia para {empleado.nombre} ya está registrada.')
        
        if se_registro_asistencia:
            messages.success(request, 'Asistencia registrada con éxito para los empleados seleccionados.')
        return redirect('asistencia:registrar_asistencia')

    empleados_con_asistencias = [
        {
            'empleado': empleado,
            'asistencia': empleado.asistencias.filter(fecha=today).first(),
        }
        for empleado in empleados
    ]

    return render(request, 'asistencia/registrar_asistencia.html', {
        'empleados_con_asistencias': empleados_con_asistencias,
        'today': today,
    })

def lista_asistencias(request):
    asistencias = Asistencia.objects.all().order_by('-fecha')
    return render(request, 'asistencia/lista_asistencias.html', {'asistencias': asistencias})
