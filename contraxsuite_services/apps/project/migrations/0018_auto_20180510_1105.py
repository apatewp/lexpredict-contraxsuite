# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-10 11:05
from __future__ import unicode_literals

import apps.common.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_delete_reviewstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(blank=True, default=apps.common.models.get_default_status, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.ReviewStatus'),
        ),
    ]
