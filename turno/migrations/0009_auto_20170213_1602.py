# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0008_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='nombre',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
