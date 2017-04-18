from dal import autocomplete
from django import forms
from django.db.models.query_utils import Q

from turno.constants import EstadoBox, EstadoTicket
from turno.models import Ticket, Sector, Box


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['fecha', 'hora']
        widgets = {
            'cliente': autocomplete.ModelSelect2(url='cliente-autocomplete')
        }


class BoxAtencionForm(forms.Form):
    sector = forms.CharField(max_length=40, required=False)
    box = forms.CharField(max_length=50, required=False)
    estado = forms.ChoiceField(choices=EstadoBox.LISTA_ESTADOS, )
    cliente = forms.CharField(max_length=50, required=False)
    derivar_a = forms.ModelChoiceField(Sector.objects, required=False)
    documento = forms.CharField(max_length=30, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(BoxAtencionForm, self).__init__(*args, **kwargs)
        self.fields['sector'].widget.attrs['readonly'] = True
        self.fields['box'].widget.attrs['readonly'] = True
        self.fields['estado'].widget.attrs['disabled'] = True
        self.fields['cliente'].widget.attrs['readonly'] = True
        self.fields['cliente'].widget.attrs['style'] = 'width:300px'
        self.fields['documento'].widget.attrs['readonly'] = True

        self.fields['sector'].initial = Sector.objects.filter(box__funcionario__usuario=self.request.user).first()
        box = Box.objects.filter(funcionario__usuario=self.request.user).first()
        if box:
            self.fields['box'].initial = box
            self.fields['estado'].initial = box.estado
        ticket = Ticket.objects.filter(estado__in=[EstadoTicket.LLAMADO,EstadoTicket.ATENDIDO],
                                       sector=self.fields['sector'].initial, box=box).first()

        if ticket:
            self.fields['cliente'].initial = ticket.cliente
            self.fields['documento'].initial = ticket.cliente.documento

    def is_valid(self):
        return True
