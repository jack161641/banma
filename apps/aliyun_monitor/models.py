# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AlertMessage(models.Model):
    userId = models.CharField(max_length=100,verbose_name=u"用户ID")
    alertName = models.CharField(max_length=100,verbose_name=u"报警名称")
    timestamp = models.CharField(max_length=100, verbose_name=u"发生报警的时间戳")
    alertState = models.CharField(max_length=100, verbose_name=u"报警状态")
    instanceId = models.CharField(max_length=100, verbose_name=u"发生报警的对象")
    expression = models.CharField(max_length=100, verbose_name=u"报警条件")
    curValue = models.CharField(max_length=100, verbose_name=u"监控项当前值")
    metricName = models.CharField(max_length=100, verbose_name=u"监控项名称")
    metricProject = models.CharField(max_length=100, verbose_name=u"产品名称")


    class Meta:
        verbose_name = u"告警信息"
        verbose_name_plural=verbose_name