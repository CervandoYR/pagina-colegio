from django.db import models

class Encuesta(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    calificacion_atencion = models.CharField(max_length=20)  
    escuchado = models.BooleanField()  
    recomendacion = models.BooleanField() 
    calificacion_instalaciones = models.CharField(max_length=20)  
    experiencia_general = models.CharField(max_length=20)  

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"

    def save(self, *args, **kwargs):
        # Guardar en la base de datos postgreSQL
        super().save(*args, **kwargs)
        
