from django.db import models
from cloudinary.models import CloudinaryField

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    invitados_min = models.IntegerField(default=0)
    invitados_max = models.IntegerField(default=0)
    
    ESTADOS = [
        ('pendiente', 'Pendiente de Pago'),
        ('al_corriente', 'Al Corriente'),
        ('prorroga', 'Prórroga'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return self.nombre

class Pago(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='pagos')
    comprobante = CloudinaryField("Comprobante", folder="pagos_graduacion")
    cantidad_boletos = models.IntegerField(default=1, verbose_name="Cantidad de Boletos")
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno.nombre} - {self.cantidad_boletos} boletos"
