# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0009_auto_20170130_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='androidId',
            new_name='android_id',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='buildNumber',
            new_name='build_number',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='osVersion',
            new_name='operating_system_version',
        ),
        migrations.AlterField(
            model_name='device',
            name='facility',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facility.Facility'),
        ),
    ]
