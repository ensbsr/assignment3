# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0003_course_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
        migrations.AddField(
            model_name='course',
            name='enrolled_students',
            field=models.ManyToManyField(to='formapp.Student', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='enrolled_courses',
            field=models.ManyToManyField(to='formapp.Course', blank=True),
            preserve_default=True,
        ),
    ]
