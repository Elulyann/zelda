# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20150609_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civility',
            name='complete_name_fr',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='civi',
        ),
        migrations.AddField(
            model_name='contact',
            name='civility',
            field=models.ForeignKey(to='contacts.Civility', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='zip_code',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]
