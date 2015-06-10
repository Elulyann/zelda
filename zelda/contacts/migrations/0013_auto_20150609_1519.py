# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20150609_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='zip_code',
            field=models.CharField(max_length=5, default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='categories',
            field=models.ManyToManyField(to='contacts.Categorie'),
        ),
    ]
