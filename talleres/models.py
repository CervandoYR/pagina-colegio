from django.db import models
from django.core.exceptions import ValidationError

class InscripcionTaller(models.Model):
    TALLER_CHOICES = [
        ('ajedrez', 'Taller de Ajedrez'),
        ('teatro', 'Taller de Teatro'),
        ('oratoria', 'Taller de Oratoria'),
        ('danza', 'Taller de Danza'),
    ]
    GRADO_CHOICES = [(str(i), f"{i}°") for i in range(1, 6)]
    SECCION_CHOICES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    numero = models.CharField(max_length=9, unique=True)
    apoderado = models.CharField(max_length=100)
    grado = models.CharField(max_length=10, choices=GRADO_CHOICES)
    seccion = models.CharField(max_length=10, choices=SECCION_CHOICES)
    taller = models.CharField(max_length=20, choices=TALLER_CHOICES)
    horario = models.CharField(max_length=50)

    def clean(self):
        if len(self.numero) != 9 or not self.numero.isdigit():
            raise ValidationError('El número debe tener 9 dígitos y ser numérico.')

        if not (self.correo.endswith('@gmail.com') or self.correo.endswith('@hotmail.com')):
            raise ValidationError('El correo debe ser de un formato estándar (ej. ejemplo@gmail.com o ejemplo@hotmail.com).')
    
    def save(self, *args, **kwargs):
        # Guardar en la base de datos postgreSQL
        super().save(*args, **kwargs)
        
