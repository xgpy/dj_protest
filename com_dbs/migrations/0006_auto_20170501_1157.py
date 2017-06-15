# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_dbs', '0005_auto_20170426_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='python_title',
            name='note_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='python_title',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
