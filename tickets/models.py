from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Ticket(models.Model):
    nombre_alumno = models.CharField(max_length=100)
    id_alumno = models.IntegerField(null=True, blank=True)
    ticket = CloudinaryField(
        "Archivo de imagen",
        folder="tickets"
    )