# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-24 13:26
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_recommend',
            field=models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570'),
        ),
    ]