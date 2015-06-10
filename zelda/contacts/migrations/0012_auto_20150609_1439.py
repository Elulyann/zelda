# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20150609_1437'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Civility',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='civility',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='title',
            old_name='title',
            new_name='name',
        ),
    ]
