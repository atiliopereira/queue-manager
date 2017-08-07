from dal import autocomplete

from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from django.contrib.auth.models import User
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

    class Media:
        js = ('js/login.js',)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        usuario = User.objects.get(username=cleaned_data.get('username'))
        if not Box.objects.filter(funcionario__usuario=usuario) and cleaned_data.get('sitio') == 'Box':
            raise ValidationError('Debe tener asignado un box, comuniquese con administración para se le asigne uno')
        return cleaned_data







