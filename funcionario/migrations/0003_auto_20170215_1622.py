# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_cargo_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, related_name='usuario', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
