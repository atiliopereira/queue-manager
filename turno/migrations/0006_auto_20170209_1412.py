# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.views.generic.dates
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0005_auto_20170208_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='estado',
            field=models.CharField(default='PENDIENTE', max_length=15, blank=True, choices=[('PENDIENTE', 'Pendiente'), ('ATENDIDO', 'Atendido'), ('CERRADO', 'Cerrado'), ('CANCELADO', 'Cancelado')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fecha',
            field=models.DateField(default=django.views.generic.dates.timezone_today, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora',
            field=models.TimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
