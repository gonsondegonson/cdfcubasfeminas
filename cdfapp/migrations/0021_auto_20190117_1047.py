# Generated by Django 2.1 on 2019-01-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdfapp', '0020_auto_20181227_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='url_calendar',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='url_classification',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='url_results',
            field=models.URLField(blank=True, null=True),
        ),
    ]