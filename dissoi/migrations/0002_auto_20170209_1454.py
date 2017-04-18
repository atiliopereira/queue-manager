# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_cargo_activo'),
        ('dissoi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sesion',
            name='usuario',
        ),
        migrations.AddField(
            model_name='sesion',
            name='funcionario',
            field=models.ForeignKey(default=None, to='funcionario.Funcionario'),
            preserve_default=False,
        ),
    ]
