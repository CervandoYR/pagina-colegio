from django.contrib import admin
from django.urls import include, path
from myproject.vista import index  # Verifica que `index` está correctamente importado.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('admision/', include('admisiones.urls')),
    path('talleres/', include('talleres.urls')),
    path('encuesta/', include('encuesta.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('marcacion/', include('marcacion.urls')),
    path('registro/', include('registro.urls')),
    path('asistencia/', include('asistencia.urls')),
    path('dashboard/', include('dashboard.urls')),
    
]
