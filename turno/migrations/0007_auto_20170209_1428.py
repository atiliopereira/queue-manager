# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_cargo_activo'),
        ('turno', '0006_auto_20170209_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='atendido_por',
            field=models.ForeignKey(null=True, related_name='funcionario_box', to='funcionario.Funcionario', blank=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='creado_por',
            field=models.ForeignKey(null=True, related_name='funcionario_ticket', to='funcionario.Funcionario', blank=True),
        ),
    ]
