# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20150609_1411'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CivilityName',
            new_name='Civility',
        ),
    ]
