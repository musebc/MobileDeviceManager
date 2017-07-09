# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device', '0001_initial'),
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='facility',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facility.facility'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]