# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 06:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploadimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=30)),
                ('usr_image', models.ImageField(upload_to='pics')),
                ('usr_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
