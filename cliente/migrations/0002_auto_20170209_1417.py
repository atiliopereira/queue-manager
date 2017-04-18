# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.CharField(unique=True, null=True, max_length=25),
        ),
    ]
