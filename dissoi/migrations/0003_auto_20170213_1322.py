# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dissoi', '0002_auto_20170209_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sesion',
            options={'verbose_name_plural': 'Sesiones'},
        ),
        migrations.AlterField(
            model_name='sesion',
            name='hora_logout',
            field=models.DateTimeField(null=True),
        ),
    ]
