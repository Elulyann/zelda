# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_contact_civi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='civility',
        ),
        migrations.AlterField(
            model_name='contact',
            name='civi',
            field=models.TextField(max_length=100, choices=[('MADEMOISELLE', 'Mademoiselle'), ('MADAME', 'Madame'), ('MONSIEUR', 'Monsieur')]),
        ),
    ]
