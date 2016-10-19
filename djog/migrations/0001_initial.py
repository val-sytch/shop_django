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
                'verbose_name': 'Breed',
                'verbose_name_plural': 'Breeds',
            },
        ),
        migrations.CreateModel(
            name='Customers',
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
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.SlugField(verbose_name='Item alias')),
                ('description', models.TextField(max_length=1000, verbose_name='Short description')),
                ('image', models.CharField(max_length=100, verbose_name='Image URL')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('availability', models.BooleanField(default=True, verbose_name='Availability')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('breed', models.ForeignKey(to='djog.Breeds')),
            ],
            options={
                'verbose_name': 'Dog',
                'verbose_name_plural': 'Dogs',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1, choices=[(1, 'Created'), (2, 'In Progress'), (3, 'Waiting for payment'), (4, 'Waiting for shipped'), (5, 'Waiting for arrived'), (6, 'Arrived'), (7, 'Closed')])),
                ('name', models.CharField(max_length=10, verbose_name='Name')),
                ('surname', models.CharField(max_length=10, verbose_name='Surname')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('email', models.EmailField(max_length=20, null=True, verbose_name='E-mail')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to='djog.Customers', null=True, blank=True)),
                ('item', models.ForeignKey(to='djog.Dogs')),
            ],
        ),
    ]
