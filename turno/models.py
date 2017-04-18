import datetime

from django.db import models
from django.utils.timezone import utc
from django.views.generic.dates import timezone_today

from cliente.models import Cliente
from funcionario.models import Funcionario
from turno.constants import EstadoTicket, EstadoBox


def get_time_diff(despues, antes):
    if antes:
        return (despues.replace(tzinfo=utc) - antes).total_seconds()


class Sector(models.Model):
    class Meta:
        verbose_name_plural = 'Sectores'

    nombre = models.CharField(max_length=40, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Box(models.Model):
    class Meta:
        verbose_name_plural = 'Boxes'

    nombre = models.CharField(max_length=50, unique=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name='funcionario', null=True,
                                    blank=True)
    estado = models.CharField(choices=EstadoBox.LISTA_ESTADOS, max_length=20, default=EstadoBox.INHABILITADO)
    sector = models.ForeignKey(Sector, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Atencion(Box):
    class Meta:
        proxy = True
        verbose_name_plural = 'Atenciones'
        verbose_name = 'Atención'


class Ticket(models.Model):
    fecha = models.DateField(default=timezone_today, blank=True)
    hora = models.TimeField(default=datetime.datetime.now, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='cliente')
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, related_name='ticket_sector')
    box = models.ForeignKey('Box', on_delete=models.PROTECT, related_name='ticket_box', null=True, blank=True)
    estado = models.CharField(choices=EstadoTicket.LISTA_ESTADOS, max_length=15, default=EstadoTicket.PENDIENTE,
                              blank=True)
    hora_llamado = models.TimeField(null=True, blank=True)
    hora_atencion = models.TimeField(null=True, blank=True)
    hora_cierre = models.TimeField(null=True, blank=True)
    atendido_por = models.ForeignKey(Funcionario, null=True, blank=True, related_name='funcionario_box')
    creado_por = models.ForeignKey(Funcionario, null=True, blank=True, related_name='funcionario_ticket')
    ticket_padre = models.ForeignKey('Ticket',null=True,blank=True)

    def __str__(self):
        return '%s' % self.pk

    def tiempo_atencion(self):
        return get_time_diff(self.hora_atencion, self.hora)
