# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=30)),
                ('course_code', models.CharField(max_length=3)),
                ('course_classroom', models.CharField(max_length=30)),
                ('course_time', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('office_details', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='formapp.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='formapp.Teacher'),
            preserve_default=True,
        ),
    ]
