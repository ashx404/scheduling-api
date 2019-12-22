from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore

sched = BackgroundScheduler()
sched.start()


def callAPI(url):
    req = requests.get(url)
    print(req.status_code)


def schedulingAPI(request):
    x = 5
    timeArr = request.GET.get('t').split(':')
    print(timeArr)
    dateArr = request.GET.get('d').split('-')
    print(dateArr)
    inputUri = request.GET.get('url')
    print(int(timeArr[0]))
    print(type(int(timeArr[0])))
    if int(timeArr[0]) < 0 or int(timeArr[0]) > 23 or int(timeArr[1]) > 59 or int(timeArr[1]) < 0:
        return JsonResponse({
            "Error": "Invalid Time"
        })

    if int(dateArr[0]) > 31 or int(dateArr[0]) < 0 or int(dateArr[1]) < 1 or int(dateArr[1]) > 12:
        return JsonResponse({
            "Error": "Invalid Date"
        })

    sched.add_job(callAPI, 'cron', [inputUri], year=dateArr[2], month=dateArr[1],
                  day=dateArr[0], hour=timeArr[0], minute=timeArr[1], timezone='Asia/Kolkata')
    print(sched.print_jobs())
    return JsonResponse({
        "status": "OK"
    })


def ping(request):
    return JsonResponse({"status": "OK"})
