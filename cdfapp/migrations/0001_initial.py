# Generated by Django 2.1 on 2018-10-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('stylesheet', models.CharField(max_length=100)),
                ('instagram_href', models.URLField()),
                ('instagram_text', models.CharField(max_length=100)),
                ('facebook_href', models.URLField()),
                ('facebook_text', models.CharField(max_length=100)),
                ('twitter_href', models.URLField()),
                ('twitter_text', models.CharField(max_length=100)),
                ('google_href', models.URLField()),
                ('google_text', models.CharField(max_length=100)),
                ('youtube_href', models.URLField()),
                ('youtube_text', models.CharField(max_length=100)),
                ('sendmail_href', models.EmailField(max_length=254)),
                ('sendmail_text', models.CharField(max_length=100)),
            ],
        ),
    ]
