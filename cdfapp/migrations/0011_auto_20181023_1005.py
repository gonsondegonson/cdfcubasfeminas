# Generated by Django 2.1 on 2018-10-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdfapp', '0010_auto_20181023_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='href',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='galleryobject',
            name='href',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='galleryobject',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
