# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20150609_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='civility',
            old_name='name',
            new_name='title',
        ),
    ]
