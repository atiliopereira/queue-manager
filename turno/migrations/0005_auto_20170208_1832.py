# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0004_auto_20170208_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='sector',
            field=models.ForeignKey(to='turno.Sector', null=True),
        ),
    ]
