# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_auto_20151228_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='enrolled_students',
        ),
        migrations.RemoveField(
            model_name='student',
            name='enrolled_courses',
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='formapp.Student'),
            preserve_default=True,
        ),
    ]
