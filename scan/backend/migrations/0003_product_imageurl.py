# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_comment_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageUrl',
            field=models.CharField(default='http://placehold.it/350x150', max_length=1024),
        ),
    ]