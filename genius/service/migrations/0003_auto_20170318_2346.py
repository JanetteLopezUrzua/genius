# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 23:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_room_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='question_photo',
            new_name='room_photo',
        ),
    ]
