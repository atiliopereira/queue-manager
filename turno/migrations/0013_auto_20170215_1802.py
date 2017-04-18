# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0012_auto_20170215_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_padre',
            field=models.ForeignKey(blank=True, null=True, to='turno.Ticket'),
        ),
        migrations.AlterField(
            model_name='box',
            name='estado',
            field=models.CharField(max_length=20, choices=[('LIBRE', 'Libre'), ('OCUPADO', 'Ocupado'), ('INHABILITADO', 'Inhabilitado'), ('ASIGNADO', 'Asignado')], default='INHABILITADO'),
        ),
    ]
