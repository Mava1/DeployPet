from django.db import models
from django.db.models import Model

class Producto(Model):
     
    tipo_choices = [
        ("seco", "Productos Secos"),
        ("humedo", "Productos Humedos"),
        ("juego", "Jueguetes")
        
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=tipo_choices)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)


    def __str__(self):
        return self.nombre

    class Meta:
         db_table = "productos_table"