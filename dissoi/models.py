from django.contrib.auth.models import User
from django.db import models
import datetime

from funcionario.models import Funcionario


class Sesion(models.Model):
    class Meta:
        verbose_name_plural = 'Sesiones'

    funcionario = models.ForeignKey(Funcionario)
    fecha_login = models.DateTimeField(default=datetime.datetime.now)
    hora_logout = models.DateTimeField(null=True)

    def __str__(self):
        return self.funcionario.__str__()
