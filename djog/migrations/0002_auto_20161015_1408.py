# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogs',
            old_name='breeds',
            new_name='breed',
        ),
    ]
