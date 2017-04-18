# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('documento', models.CharField(max_length=25, unique=True)),
                ('fecha_ingreso', models.DateField(null=True)),
                ('activo', models.BooleanField(default=True)),
                ('cargo', models.ForeignKey(to='funcionario.Cargo', related_name='cargo', on_delete=django.db.models.deletion.PROTECT)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='usuario', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
    ]
