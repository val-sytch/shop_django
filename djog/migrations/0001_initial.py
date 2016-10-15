# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=120, verbose_name='Breed name')),
                ('alias', models.SlugField(verbose_name='Breed alias')),
            ],
            options={
                'verbose_name_plural': 'Breeds',
                'verbose_name': 'Breed',
            },
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000, verbose_name='Short description')),
                ('image', models.CharField(max_length=100, verbose_name='Image URL')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('alias', models.SlugField(verbose_name='Item alias')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('breeds', models.ForeignKey(to='djog.Breeds')),
            ],
        ),
        migrations.CreateModel(
            name='SingUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=18)),
                ('regis_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
