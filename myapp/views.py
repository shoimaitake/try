from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.utils import timezone
from django.template import loader
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
import datetime
import time
import json


# Create your views here.
from .models import AvailableSlot, Subject, CustomUser, Schedule

from .forms import SlotForm

@login_required
def HomeView(request):
    user = request.user
    schedules = Schedule.objects.filter(teacher=user) | Schedule.objects.filter(learner=user)
    return render(request, 'myapp/home.html', {'schedules': schedules})

def ProfileView(request):
    user = request.user
    return render(request, "myapp/profile.html", {'user': user})

def SlotsView(request):
    get_token(request)

    template = loader.get_template("myapp/slots.html")
    return HttpResponse(template.render())

def AddSlotView(request):
    if request.method == "GET":
        # GETは対応しない
        raise Http404()

    # JSONの解析
    datas = json.loads(request.body)

    # UNIXタイムスタンプを文字列形式の日時に変換
    formatted_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datas["start_time"] / 1000))
    formatted_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datas["end_time"] / 1000))

    # 登録処理
    available_slot = AvailableSlot(
        teacher=request.user,  # ログイン中のユーザーを取得
        start_time=formatted_start_time,
        end_time=formatted_end_time,
    )
    available_slot.save()

    # 空を返却
    return HttpResponse("")

def DeleteSlotView(request):
    return 

def GetSlotView(request):
    if request.method == "GET":
        # GETは対応しない
        raise Http404()
    
    # JSONの解析
    datas = json.loads(request.body)

    # UNIXタイムスタンプを文字列形式の日時に変換
    formatted_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datas["start_time"] / 1000))
    formatted_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datas["end_time"] / 1000))

    # FullCalendarの表示範囲のみ表示
    slots = AvailableSlot.objects.filter(
        start_time__lt=formatted_end_time, end_time__gt=formatted_start_time
    )

    # fullcalendarのため配列で返却
    slot_list = []
    for slot in slots:
        slot_list.append(
            {
                "title": "slot",
                "start": slot.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end": slot.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return JsonResponse(slot_list, safe=False)
    

def ReserveView(request):
    template = loader.get_template("myapp/reserve.html")
    return HttpResponse(template.render())
