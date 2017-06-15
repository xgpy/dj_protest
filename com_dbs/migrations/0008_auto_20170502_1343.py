# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_dbs', '0007_auto_20170501_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='python_title',
            name='note_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
