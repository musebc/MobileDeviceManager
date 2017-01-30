# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
        ('device', '0004_auto_20170130_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='downloadedApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downloadedDate', models.DateTimeField(auto_now_add=True)),
                ('renewalDate', models.DateField(default=django.utils.timezone.now)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Application')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
            ],
        ),
    ]