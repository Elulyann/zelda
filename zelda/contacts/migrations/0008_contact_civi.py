# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20150609_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='civi',
            field=models.TextField(choices=[('MADEMOISELLE', 'Mademoiselle'), ('MADAME', 'Madame'), ('MONSIEUR', 'Monsieur')], default='Non defini'),
        ),
    ]
