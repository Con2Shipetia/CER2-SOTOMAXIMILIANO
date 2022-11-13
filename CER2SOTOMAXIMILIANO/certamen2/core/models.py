from django.db import models

# Create your models here.

class Residencia(models.Model):
    numero = models.IntegerField(primary_key=True)
    dueno = models.CharField(max_length=40)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=60)


class Correspondencia(models.Model):
    fecha_recepcion = models.DateField(null=True, blank=True)
    conserje = models.CharField(max_length=50)
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    numresidencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)

