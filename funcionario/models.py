from django.contrib.auth.models import User
from django.db import models


class Cargo(models.Model):
    nombre = models.CharField(max_length=25)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



class Funcionario(models.Model):
    documento = models.CharField(max_length=25, unique=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='cargo')
    fecha_ingreso = models.DateField(null=True)
    activo = models.BooleanField(default=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, related_name='usuario',null=True)

    def __str__(self):

        if self.usuario.first_name and self.usuario.last_name:
            return '%s %s'%(self.usuario.first_name,self.usuario.last_name)
        return '%s'%(self.usuario)
