# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('com_dbs', '0004_comment_python_prereply_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_python',
            name='prereply_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
