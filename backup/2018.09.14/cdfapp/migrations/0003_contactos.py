# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cdfapp', '0002_auto_20180601_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('fecha_peticion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_respuesta', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
