from django.contrib import admin

from cliente.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','documento','es_cliente','activo']
    search_fields = ['nombre','apellido','documento']
    ordering = ['nombre','apellido']







