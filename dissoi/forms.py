from dal import autocomplete

from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from django.utils.translation import ugettext_lazy as _

from turno.constants import EstadoBox
from turno.models import Box

class Sitio:
    ADMIN = 'A'
    BOX = 'B'
    TICKET = 'T'

    CHOICES = [
        (ADMIN, 'Administración'),
        (BOX, 'Box'),
        (TICKET, 'Tickets')
    ]

class LoginForm(AdminAuthenticationForm):
    sitio = forms.ChoiceField(choices=Sitio.CHOICES, widget=forms.RadioSelect)
    box = forms.ModelChoiceField(queryset=Box.objects.filter(activo=True, estado=EstadoBox.INHABILITADO), required=False,
                                 widget=autocomplete.ModelSelect2(url='box_inhabilitado-autocomplete')
                                 )

    class Media:
        js = ('js/login.js',)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if cleaned_data.get('sitio') == Sitio.BOX and not cleaned_data.get('box', ''):
            raise ValidationError('Debe seleccionar un box')
        return cleaned_data







