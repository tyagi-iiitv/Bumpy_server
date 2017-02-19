# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bumps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.FloatField()),
                ('lattitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, serialize=False, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'')),
            ],
        ),
    ]
