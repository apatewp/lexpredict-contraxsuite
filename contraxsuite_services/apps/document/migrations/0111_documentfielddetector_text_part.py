# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-12 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0110_remove_temporary_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfielddetector',
            name='text_part',
            field=models.CharField(choices=[('FULL', 'FULL'), ('BEFORE_REGEXP', 'BEFORE_REGEXP'), ('AFTER_REGEXP', 'AFTER_REGEXP')], db_index=True, default='FULL', max_length=30),
        ),
    ]