# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('com_dbs', '0003_comment_python'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_python',
            name='prereply_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 26, 11, 50, 44, 392000)),
        ),
    ]
