# Generated by Django 2.1 on 2019-03-08 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdfapp', '0006_clubequipement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teaminstallation',
            old_name='tittle',
            new_name='title',
        ),
    ]