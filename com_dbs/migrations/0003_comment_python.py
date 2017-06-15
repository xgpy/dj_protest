# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_dbs', '0002_blogs_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment_python',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_user', models.CharField(max_length=50)),
                ('comment_cont', models.CharField(max_length=500)),
                ('comment_date', models.DateTimeField(auto_now=True)),
                ('comment_reply', models.CharField(default=b'0', max_length=50)),
                ('comment_level', models.IntegerField()),
                ('comment_title', models.ForeignKey(to='com_dbs.python_title')),
            ],
        ),
    ]
