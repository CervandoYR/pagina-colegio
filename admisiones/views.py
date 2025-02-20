from django.shortcuts import render
from .forms import FormularioAdmisionForm  # Importa tu formulario

def admision_view(request):
    if request.method == 'POST':
        form = FormularioAdmisionForm(request.POST)  # Usa tu formulario personalizado
        if form.is_valid():
            form.save()  # Guarda el formulario en la base de datos
            # Redirigir a la misma página
            return render(request, 'admisiones/formularioAdmision.html', {'form': FormularioAdmisionForm(), 'success': True})  # Reinicia el formulario
    else:
        form = FormularioAdmisionForm()  # Crea una instancia vacía del formulario

    return render(request, 'admisiones/formularioAdmision.html', {'form': form})  # Pasa el formulario a la plantilla
