from django.conf.urls import url
from django.contrib import admin

# Register your models here.
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.html import format_html

from funcionario.models import Funcionario
from turno.forms import TicketForm
from turno.models import Sector, Box, Ticket, Producto

from django.contrib import messages


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'sector', 'estado', 'funcionario']
    fields = ['nombre', 'funcionario', 'estado', 'sector', 'activo']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'producto', 'sector', 'box']
    fields = ['cliente', 'producto', 'sector']
    search_fields = ['cliente__documento', 'cliente__nombre', 'cliente__apellido']

    form = TicketForm

    def add_view(self, request, form_url='', extra_context=None):
        if not Funcionario.objects.filter(usuario=request.user).exists():
            self.message_user(request, 'Este usuario debe tener un Funcionario asociado', level=messages.WARNING)
            info = self.model._meta.app_label, self.model._meta.model_name
            return HttpResponseRedirect(reverse('admin:%s_%s_changelist' % info))
        return super(TicketAdmin, self).add_view(request, form_url=form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creado_por = Funcionario.objects.get(usuario=request.user)
        return super(TicketAdmin, self).save_model(request, obj, form, change)

