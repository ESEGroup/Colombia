# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0005_auto_20161115_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
