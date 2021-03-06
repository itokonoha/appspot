# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment_date',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='record_creation_date',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start_address',
            field=localflavor.us.models.USZipCodeField(help_text='', max_length=10),
        ),
    ]
