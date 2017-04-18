# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0003_auto_20170130_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name': 'Atención',
                'verbose_name_plural': 'Atenciones',
            },
            bases=('turno.box',),
        ),
    ]
