# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0011_ticket_hora_llamado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='estado',
            field=models.CharField(max_length=20, default='LIBRE', choices=[('LIBRE', 'Libre'), ('OCUPADO', 'Ocupado'), ('INHABILITADO', 'Inhabilitado'), ('ASIGNADO', 'Asignado')]),
        ),
    ]
