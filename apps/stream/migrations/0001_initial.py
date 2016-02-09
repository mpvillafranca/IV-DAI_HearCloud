# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('audio_file', models.FileField(upload_to=b'uploads')),
                ('genre', models.CharField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
