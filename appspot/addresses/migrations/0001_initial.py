# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_type', models.CharField(choices=[('HOME', 'Home'), ('WORK', 'Work'), ('OTHER', 'Other')], max_length=100, verbose_name='Address type')),
                ('location_address', localflavor.us.models.USZipCodeField(help_text='', max_length=10)),
                ('address_label', models.CharField(max_length=100, verbose_name='Address label')),
                ('record_owner', models.CharField(max_length=100, verbose_name='Record owner')),
                ('record_creation_date', models.DateField(help_text='')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='companies.Company', verbose_name='Company')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='person.Person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
    ]