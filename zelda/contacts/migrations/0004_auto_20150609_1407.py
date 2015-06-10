# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20150609_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='civilityname',
            name='complete_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='civilityname',
            name='complete_name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
