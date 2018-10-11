# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdfapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='preferente',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='resumen',
            field=models.CharField(max_length=400),
        ),
    ]
