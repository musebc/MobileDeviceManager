# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_auto_20170222_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portaluser',
            name='facility',
            field=models.ManyToManyField(to='facility.Facility'),
        ),
    ]
