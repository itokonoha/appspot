# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_items', '0002_auto_20171005_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_items',
            name='service_date',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='invoice_items',
            name='service_end_date',
            field=models.DateField(auto_now_add=True, help_text=''),
        ),
    ]
