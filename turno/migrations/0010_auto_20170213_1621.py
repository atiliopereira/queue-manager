# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0009_auto_20170213_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='estado',
            field=models.CharField(default='PENDIENTE', choices=[('PENDIENTE', 'Pendiente'), ('LLAMADO', 'Llamado'), ('ATENDIDO', 'Atendido'), ('CERRADO', 'Cerrado'), ('CANCELADO', 'Cancelado')], max_length=15, blank=True),
        ),
    ]
