from django.contrib import admin

from dissoi.models import Sesion


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ['funcionario','fecha_login','hora_logout']
    readonly_fields = ['funcionario','fecha_login']
    fields = ['funcionario','fecha_login','hora_logout']

    def has_add_permission(self, request):
        return False


    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        return []