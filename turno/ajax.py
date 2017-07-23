from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query_utils import Q
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_GET

from cliente.models import Cliente
from dissoi.views import logout_user
from turno.constants import EstadoTicket, EstadoBox
from turno.models import Ticket, Box, Sector
from django.core import serializers
import json
import datetime

@require_GET
def get_tickets(request):
    tickets = Ticket.objects.filter(estado=EstadoTicket.PENDIENTE).order_by('id')
    #LOS LLAMADOS TIENEN QUE SER SOLO LOS QUE ESTAN EN UN BOX.
    llamados = Ticket.objects.filter(estado=EstadoTicket.ATENDIDO)

    llamados_dict = []
    for llamado in llamados:
        llamados_dict.append({
            'id': llamado.id,
            'cliente': llamado.cliente.nombre + ' ' + llamado.cliente.apellido,
            'sector': llamado.sector.nombre,
            'box': llamado.box.nombre,
        })
    tickets_dict = []
    nombre_box = ""
    for ticket in tickets:
        if ticket.box:
            nombre_box = ticket.box.nombre
        tickets_dict.append({
            'id': ticket.id,
            'cliente': ticket.cliente.nombre + ' ' + ticket.cliente.apellido,
            'sector': ticket.sector.nombre,
            'box': nombre_box,
        })

    return JsonResponse({'tickets': tickets_dict, 'llamados': llamados_dict})


def box_atencion_ajax(request):
    sector = request.GET.get('sector', '')
    box = request.GET.get('box', '')
    ticket_id = request.GET.get('id', '')

    if sector:
        sector = Sector.objects.get(nombre=sector)
    if box:
        box = Box.objects.get(nombre=box)
    result = {}
    if box and sector:
        if box.estado == EstadoBox.LIBRE:
            ticket = Ticket.objects.get(id=ticket_id)
            if ticket and ticket.box is None:
                if ticket.estado == EstadoTicket.PENDIENTE:
                    ticket.estado = EstadoTicket.LLAMADO
                    ticket.box = box
                    ticket.hora_llamado = timezone.now()
                    ticket.save()
                    box.estado = EstadoBox.ASIGNADO
                    box.save()
                result.update({
                    'cliente': str(ticket.cliente),
                    'documento': ticket.cliente.documento,
                })
    return JsonResponse(result)
