# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('com_dbs', '0006_auto_20170501_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='python_stru',
            name='maintitle',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='python_stru',
            name='title',
            field=models.CharField(default=datetime.datetime(2017, 5, 1, 14, 49, 28, 320000), max_length=100),
            preserve_default=False,
        ),
    ]
