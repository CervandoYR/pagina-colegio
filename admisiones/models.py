from django.db import models

class FormularioAdmision(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('DNI', 'DNI'),
        ('CARNET', 'Carnet de Extranjería'),
    ]
    NACIONALIDAD_CHOICES = [
        ('PE', 'Perú'),
        ('VE', 'Venezuela'),
    ]
    
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    tipo_documento = models.CharField(max_length=10, choices=DOCUMENT_TYPE_CHOICES)
    numero_documento = models.CharField(max_length=30, unique=True)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=2, choices=NACIONALIDAD_CHOICES)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])

    def save(self, *args, **kwargs):
        # Guardar en la base de datos por defecto (PostgreSQL)
        super().save(*args, **kwargs)
