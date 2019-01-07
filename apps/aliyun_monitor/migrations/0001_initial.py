# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-06 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=100, verbose_name='\u7528\u6237ID')),
                ('alertName', models.CharField(max_length=100, verbose_name='\u62a5\u8b66\u540d\u79f0')),
                ('timestamp', models.CharField(max_length=100, verbose_name='\u53d1\u751f\u62a5\u8b66\u7684\u65f6\u95f4\u6233')),
                ('alertState', models.CharField(max_length=100, verbose_name='\u62a5\u8b66\u72b6\u6001')),
                ('instanceId', models.CharField(max_length=100, verbose_name='\u53d1\u751f\u62a5\u8b66\u7684\u5bf9\u8c61')),
                ('expression', models.CharField(max_length=100, verbose_name='\u62a5\u8b66\u6761\u4ef6')),
                ('curValue', models.CharField(max_length=100, verbose_name='\u76d1\u63a7\u9879\u5f53\u524d\u503c')),
                ('metricName', models.CharField(max_length=100, verbose_name='\u76d1\u63a7\u9879\u540d\u79f0')),
                ('metricProject', models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u544a\u8b66\u4fe1\u606f',
                'verbose_name_plural': '\u544a\u8b66\u4fe1\u606f',
            },
        ),
    ]