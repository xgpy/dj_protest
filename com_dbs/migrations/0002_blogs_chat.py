# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_dbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs_chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('chat_cont', models.CharField(max_length=500)),
                ('chat_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
