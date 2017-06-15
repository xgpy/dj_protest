# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='python_cont',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cont_title', models.CharField(max_length=100)),
                ('cont_py', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='python_stru',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='python_title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('t_level', models.IntegerField()),
                ('pre_title', models.CharField(max_length=100)),
                ('note_date', models.DateTimeField(auto_now_add=True)),
                ('visit_count', models.IntegerField()),
            ],
        ),
    ]
