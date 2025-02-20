from django.shortcuts import render
from .forms import EncuestaForm

def encuesta_view(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save() 
            return render(request, 'encuesta/encuesta.html', {'form': EncuestaForm(), 'success': True})  # Inicializa un nuevo formulario
    else:
        form = EncuestaForm()  
    return render(request, 'encuesta/encuesta.html', {'form': form}) 