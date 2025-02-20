from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

class Asistencia(models.Model):
    empleado = models.ForeignKey('marcacion.Empleado', related_name='asistencias', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')])
    fecha = models.DateField()
    hora_marcado = models.TimeField()

    class Meta:
        unique_together = ('empleado', 'fecha')  # Evita registros duplicados para el mismo empleado y fecha

    def save(self, *args, **kwargs):
        # Redondear la hora de marcado para eliminar los microsegundos
        self.hora_marcado = self.hora_marcado.replace(microsecond=0)
        
        if Asistencia.objects.filter(empleado=self.empleado, fecha=self.fecha).exists():
            raise ValidationError(f'Ya existe asistencia para {self.empleado.nombre} en esta fecha.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.fecha} - {self.estado}"

