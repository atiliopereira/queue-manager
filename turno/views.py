# Create your views here.
from django.core.urlresolvers import reverse
from django.db import transaction
from django.utils import timezone

from django.db.models import Q
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


class BoxListaTicketsView(TemplateView):
    template_name = 'admin/turno/box_tickets_list.html'
    tickets = None

    def get_context_data(self, **kwargs):
        context = super(BoxListaTicketsView, self).get_context_data(**kwargs)
        context['tickets'] = self.tickets
        return context

    def get(self, request, *args, **kwargs):

        if not Box.objects.filter(funcionario__usuario=self.request.user).exists():
            return logout_user(request)

        box = Box.objects.filter(funcionario__usuario=self.request.user)[0]
        tickets = Ticket.objects.filter(Q(estado=EstadoTicket.LLAMADO) | Q(estado=EstadoTicket.PENDIENTE)
                                        | Q(estado=EstadoTicket.ATENDIDO)).filter(sector=box.sector)
        self.tickets = tickets
        return super(BoxListaTicketsView, self).get(request, *args, **kwargs)


class BoxAtencionTemplateView(FormView):
    template_name = 'admin/turno/box/box_atencion.html'
    form_class = BoxAtencionForm
    success_url = '/turno/box_tickets_list'
    ticket = None

    def get_form_kwargs(self):
        kwargs = super(BoxAtencionTemplateView, self).get_form_kwargs()
        kwargs.update({
            'request': self.request,
            'ticket': self.ticket,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(BoxAtencionTemplateView, self).get_context_data(**kwargs)
        context['ticket_id'] = self.ticket.id
        return context

    def get(self, request, ticket_id, *args, **kwargs):
        if not Box.objects.filter(funcionario__usuario=self.request.user).exists():
            return logout_user(request)

        self.ticket = Ticket.objects.get(id=ticket_id)

        return super(BoxAtencionTemplateView, self).get(request, *args, **kwargs)

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

    def post(self, request, ticket_id, *args, **kwargs):
        documento = request.POST.get('documento', '')
        sector = request.POST.get('sector', '')
        box = request.POST.get('box', '')
        box = Box.objects.get(nombre=box)
        sector = Sector.objects.get(nombre=sector)
        derivar_a = request.POST.get('derivar_a', '')
        cliente = Cliente.objects.filter(documento=documento)
        self.ticket = Ticket.objects.get(id=ticket_id)

        if 'iniciar' in request.POST:
            if cliente:
                with transaction.atomic():
                    cliente = cliente.first()
                    ticket = self.ticket
                    box.estado = EstadoBox.OCUPADO
                    ticket.estado = EstadoTicket.ATENDIDO
                    ticket.hora_atencion = timezone.now()
                    ticket.box = box
                    ticket.save()
                    box.save()
                    messages.info(request, 'Atención Iniciada.')
                    self.success_url = '/turno/box_atencion/'+str(self.ticket.id)

        if 'finalizar' in request.POST:
            if cliente:
                with transaction.atomic():
                    cliente = cliente.first()
                    ticket = self.ticket
                    box.estado = EstadoBox.LIBRE
                    ticket.estado = EstadoTicket.CERRADO
                    ticket.hora_cierre = timezone.now()
                    ticket.save()
                    derivar_a = request.POST.get('derivar_a', '')
                    if derivar_a:
                        self.derivacion(request, ticket)
                    box.save()
                    messages.success(request, 'Atención Finalizada.')

        if 'salir' in request.POST:
            if cliente:
                with transaction.atomic():
                    ticket = self.ticket
                    if ticket:
                        ticket.estado = EstadoTicket.CERRADO
                        ticket.hora_cierre = timezone.now()
                        ticket.save()
                        derivar_a = request.POST.get('derivar_a', '')
                        if derivar_a:
                            self.derivacion(request, ticket)
            box.estado = EstadoBox.INHABILITADO
            box.save()
            messages.info(request, 'Sesión Terminada')
            self.success_url = reverse('dissoi_logout')

        if 'siguiente' in request.POST:
            with transaction.atomic():
                ticket = self.ticket
                if ticket:
                    ticket.estado = EstadoTicket.CANCELADO
                    ticket.save()
                    derivar_a = request.POST.get('derivar_a', '')
                    if derivar_a:
                        self.derivacion(request, ticket)
                    box.estado = EstadoBox.LIBRE
                    box.save()
            messages.info(request, 'Ticket Cancelado.')
        return super(BoxAtencionTemplateView, self).post(request, *args, **kwargs)
