# Generated by Django 2.1 on 2018-10-10 07:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cdfapp', '0003_auto_20181009_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('response_date', models.DateTimeField(blank=True, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdfapp.Club')),
            ],
        ),
    ]
