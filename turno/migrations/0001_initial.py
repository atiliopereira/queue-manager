# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=20, default='LIBRE', choices=[('LIBRE', 'Libre'), ('OCUPADO', 'Ocupado'), ('INHABILITADO', 'Inhabilitado')])),
                ('activo', models.BooleanField(default=True)),
                ('funcionario', models.ForeignKey(to='funcionario.Funcionario', related_name='funcionario', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('activo', models.BooleanField(default=True)),
                ('box', models.ManyToManyField(related_name='sector_box', to='turno.Box')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('hora', models.TimeField(default=django.utils.timezone.now)),
                ('estado', models.CharField(max_length=15, default='PENDIENTE', choices=[('PENDIENTE', 'Pendiente'), ('ATENDIDO', 'Atendido'), ('CERRADO', 'Cerrado'), ('CANCELADO', 'Cancelado')])),
                ('hora_atencion', models.TimeField(null=True)),
                ('hora_cierre', models.TimeField(null=True)),
                ('box', models.ForeignKey(to='turno.Box', null=True, related_name='ticket_box', on_delete=django.db.models.deletion.PROTECT)),
                ('cliente', models.ForeignKey(to='cliente.Cliente', related_name='cliente', on_delete=django.db.models.deletion.PROTECT)),
                ('sector', models.ForeignKey(to='turno.Sector', related_name='ticket_sector', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
    ]
