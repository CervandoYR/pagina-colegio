from django.shortcuts import render
from .forms import FormularioTalleresForm
from django.db import DatabaseError

def inscripcion_talleres_view(request):
    if request.method == 'POST':
        form = FormularioTalleresForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'talleres/talleres.html', {
                    'form': FormularioTalleresForm(),
                    'success': True,
                })
            except DatabaseError:
                return render(request, 'talleres/talleres.html', {
                    'form': form,
                    'success': False,
                    'error_message': 'Error al guardar los datos en la base de datos.',
                })
        else:
            return render(request, 'talleres/talleres.html', {'form': form, 'success': False})
    else:
        form = FormularioTalleresForm()

    return render(request, 'talleres/talleres.html', {'form': form})
