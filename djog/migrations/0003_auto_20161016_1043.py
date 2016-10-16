# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djog', '0002_auto_20161015_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogs',
            name='quantity',
        ),
        migrations.AddField(
            model_name='dogs',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Availability'),
        ),
    ]
