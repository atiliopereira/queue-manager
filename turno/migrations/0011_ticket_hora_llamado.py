# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0010_auto_20170213_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='hora_llamado',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
