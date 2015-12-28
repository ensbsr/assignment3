# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0005_auto_20151228_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
    ]
