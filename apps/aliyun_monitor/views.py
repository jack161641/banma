# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from .models import AlertMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def postform(request):

    if request.method == "POST":
        message = request.POST.get('message','')
        message = json.loads(message)

        print message
        Alert_Message = AlertMessage()
        Alert_Message.userId = message['userId']
        Alert_Message.alertName = message['alertName']
        Alert_Message.timestamp = message['timestamp']
        Alert_Message.alertState = message['alertState']
        Alert_Message.instanceId = message['dimensions'][0]['instanceId']
        Alert_Message.expression = message['expression']
        Alert_Message.curValue = message['curValue']
        Alert_Message.metricName = message['metricName']
        Alert_Message.metricProject = message['metricProject']

        Alert_Message.save()
    return render(request, 'monitor_form.html')

@csrf_exempt
def postapi(request):

    if request.method == "POST":
        print request.body
        message = json.loads(request.body)

        print message

        Alert_Message = AlertMessage()
        Alert_Message.userId = message['userId']
        Alert_Message.alertName = message['alertName']
        Alert_Message.timestamp = message['timestamp']
        Alert_Message.alertState = message['alertState']
        Alert_Message.instanceId = message['dimensions'][0]['instanceId']
        Alert_Message.expression = message['expression']
        Alert_Message.curValue = message['curValue']
        Alert_Message.metricName = message['metricName']
        Alert_Message.metricProject = message['metricProject']
        try:
            Alert_Message.save()
        except Exception as e:
            print('json loads exception:{}'.format(e))
        return HttpResponse(HttpResponse(message),HttpResponse.status_code)
