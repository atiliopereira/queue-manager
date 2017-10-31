# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0013_auto_20170215_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='producto',
            field=models.ForeignKey(null=True, related_name='producto', on_delete=django.db.models.deletion.PROTECT, to='turno.Producto'),
        ),
    ]
