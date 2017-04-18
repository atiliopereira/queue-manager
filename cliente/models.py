from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,null=True,blank=True)
    documento = models.CharField(max_length=25, unique=True,null=True)
    es_cliente = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s - %s' % (self.nombre, self.apellido,self.documento)
