# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 23:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0030_auto_20170327_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='facility',
        ),
    ]
