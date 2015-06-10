# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20150609_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civilityname',
            name='complete_name_en',
        ),
    ]
