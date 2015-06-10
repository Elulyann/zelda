# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('last_name', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameModel(
            old_name='Civilities',
            new_name='Civility',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='civility',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.AddField(
            model_name='contact',
            name='civility',
            field=models.ForeignKey(to='contacts.Civility'),
        ),
    ]
