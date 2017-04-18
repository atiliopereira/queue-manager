# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0002_auto_20170128_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box',
            options={'verbose_name_plural': 'Boxes'},
        ),
        migrations.AlterModelOptions(
            name='sector',
            options={'verbose_name_plural': 'Sectores'},
        ),
        migrations.AlterField(
            model_name='box',
            name='funcionario',
            field=models.ForeignKey(related_name='funcionario', on_delete=django.db.models.deletion.PROTECT, blank=True, to='funcionario.Funcionario', null=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='boxes',
            field=models.ManyToManyField(related_name='sector_box', null=True, to='turno.Box', blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='box',
            field=models.ForeignKey(related_name='ticket_box', on_delete=django.db.models.deletion.PROTECT, blank=True, to='turno.Box', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora_atencion',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora_cierre',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
