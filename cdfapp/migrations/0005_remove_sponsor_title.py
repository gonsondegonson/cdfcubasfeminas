# Generated by Django 2.1 on 2019-03-08 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdfapp', '0004_installation_iframe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='title',
        ),
    ]
