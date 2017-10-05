# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Omc_ticket',
            fields=[
                ('omc_ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_number', models.IntegerField(verbose_name='Ticket number')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
                ('date_opened', models.DateTimeField(help_text='')),
                ('label', models.CharField(max_length=100, verbose_name='Label')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('resolution', models.TextField(max_length=500, verbose_name='Resolution')),
                ('date_closed', models.DateTimeField(auto_now_add=True, help_text='')),
            ],
            options={
                'verbose_name': 'omc_ticket',
                'verbose_name_plural': 'omc_tickets',
            },
        ),
    ]