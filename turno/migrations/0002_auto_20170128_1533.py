# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='box',
            old_name='descripcion',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='sector',
            old_name='box',
            new_name='boxes',
        ),
    ]
