# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_remove_civilityname_complete_name_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilityname',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
