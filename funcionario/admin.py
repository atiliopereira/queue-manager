from django.contrib import admin

# Register your models here.
from funcionario.models import Cargo, Funcionario


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nombre','activo']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','cargo','fecha_ingreso','activo']

