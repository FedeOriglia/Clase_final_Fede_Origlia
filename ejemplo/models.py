from django.db import models

# Create your models here.

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField()
    fecha_nac =models.DateField(default=True)
    direccion = models.CharField(max_length=200)
        
    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.dni}, {self.fecha_nac}, {self.direccion}"