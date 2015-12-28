# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_auto_20151227_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='formapp.Student'),
            preserve_default=True,
        ),
    ]
