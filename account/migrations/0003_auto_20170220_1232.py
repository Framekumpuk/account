# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170215_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_text', models.CharField(max_length=200)),
                ('account_money', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
