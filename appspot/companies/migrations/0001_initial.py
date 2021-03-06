# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100, verbose_name='Prefix')),
                ('company_address', localflavor.us.models.USZipCodeField(help_text='', max_length=10)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
            },
        ),
    ]
