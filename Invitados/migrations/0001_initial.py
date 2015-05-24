# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=255)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
