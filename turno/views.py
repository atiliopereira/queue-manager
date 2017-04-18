# Create your views here.
from django.core.urlresolvers import reverse
from django.db import transaction
# from django.utils import timezone
import datetime
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from cliente.models import Cliente
from dissoi.models import Sesion
from dissoi.views import logout_user
from funcionario.models import Funcionario
from turno.constants import EstadoTicket, EstadoBox
from turno.forms import BoxAtencionForm
from turno.models import Ticket, Box, Sector
from django.contrib import messages


class ColaClienteSideTemplateView(TemplateView):
    template_name = 'colaclientes.html'


class BoxAtencionTemplateView(FormView):
    template_name = 'admin/turno/box/box_atencion.html'
    form_class = BoxAtencionForm
    success_url = '/turno/box_atencion'

    def get_form_kwargs(self):
        kwargs = super(BoxAtencionTemplateView, self).get_form_kwargs()
        kwargs.update({
            'request': self.request,
        })
        return kwargs

    def get(self, request, *args, **kwargs):

        if not Box.objects.filter(funcionario__usuario=self.request.user).exists():
            return  logout_user(request)

        sesiones = Sesion.objects.filter(funcionario__usuario=request.user, hora_logout__isnull=True)
        if not sesiones.exists():
            return logout_user(request)

        print ('probando probando',sesiones,Box.objects.filter(funcionario__usuario=self.request.user).exists())
        return super(BoxAtencionTemplateView, self).get(request,*args,**kwargs)

    def derivacion(self, request, ticket):
        derivar_a = request.POST.get('derivar_a', '')
        derivar_a = Sector.objects.get(pk=derivar_a)
        ticket_derivacion = Ticket()
        ticket_derivacion.sector = derivar_a
        ticket_derivacion.ticket_padre = ticket
        ticket_derivacion.creado_por = Funcionario.objects.get(usuario=request.user)
        ticket_derivacion.cliente = ticket.cliente
        ticket_derivacion.save()
        messages.info(request, 'Cliente derivado .')

    def post(self, request, *args, **kwargs):
        documento = request.POST.get('documento', '')
        sector = request.POST.get('sector', '')
        box = request.POST.get('box', '')
        box = Box.objects.get(nombre=box)
        sector = Sector.objects.get(nombre=sector)
        derivar_a = request.POST.get('derivar_a', '')

        cliente = Cliente.objects.filter(documento=documento)
        if 'iniciar' in request.POST:
            if cliente:
                with transaction.atomic():
                    cliente = cliente.first()
                    ticket = Ticket.objects.filter(
                        cliente=cliente, box=box, sector=sector, estado=EstadoTicket.LLAMADO).first()
                    box.estado = EstadoBox.OCUPADO
                    ticket.estado = EstadoTicket.ATENDIDO
                    ticket.hora_atencion = datetime.datetime.now()
                    ticket.save()
                    box.save()
            messages.info(request, 'Atención Iniciada.')
        if 'finalizar' in request.POST:
            if cliente:
                with transaction.atomic():
                    cliente = cliente.first()
                    ticket = Ticket.objects.filter(
                        cliente=cliente, box=box, sector=sector, estado=EstadoTicket.ATENDIDO).first()
                    box.estado = EstadoBox.LIBRE
                    ticket.estado = EstadoTicket.CERRADO
                    ticket.hora_cierre = datetime.datetime.now()
                    ticket.save()

                    if derivar_a:
                        self.derivacion(request, ticket)

                    box.save()
                    messages.success(request, 'Atención Finalizada.')
        if 'salir' in request.POST:
            if cliente:
                with transaction.atomic():
                    cliente = cliente.get()
                    ticket = Ticket.objects.filter(
                        cliente=cliente, box=box, sector=sector, estado=EstadoTicket.ATENDIDO).first()
                    if ticket:
                        ticket.estado = EstadoTicket.CERRADO
                        ticket.hora_cierre = datetime.datetime.now()
                        ticket.save()
                        derivar_a = request.POST.get('derivar_a', '')
                        if derivar_a:
                            self.derivacion(request, ticket)

            box.estado = EstadoBox.INHABILITADO
            box.save()
            messages.info(request, 'Sesión Terminada')
            self.success_url = reverse('dissoi_logout')

        if 'siguiente' in request.POST:
            if cliente:
                with transaction.atomic():
                    cliente = cliente.first()
                    ticket = Ticket.objects.filter(cliente=cliente, box=box, sector=sector, estado=EstadoTicket.LLAMADO)
                    if ticket:
                        ticket = ticket.get()
                        ticket.estado = EstadoTicket.CANCELADO
                        ticket.save()
                        box.estado = EstadoBox.LIBRE
                        box.save()
                messages.info(request, 'Ticket Cancelado.')
        return super(BoxAtencionTemplateView, self).post(request, *args, **kwargs)
