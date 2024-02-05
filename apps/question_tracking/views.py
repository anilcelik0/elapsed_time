from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.time_tracking.forms import TimeRecordForm
from apps.time_tracking.models import TimeMainTopic, TimeSubTopic
from .models import QuestionMainTopic, QuestionRecord, QuestionSubTopic
from .forms import QuestionRecordForm
import datetime
from django.utils import timezone 
from dateutil.relativedelta import relativedelta, MO
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

@login_required()
def index(request):
    if request.method == "POST":
        tform = TimeRecordForm(request.POST)
        qform = QuestionRecordForm(request.POST)
        topic_id = int(request.POST["sub_topic"])
        if tform.is_valid():
            topic = TimeSubTopic.objects.get(id=topic_id)
            obj = tform.save(commit=False)
            obj.topic = topic
            obj.save()
        if qform.is_valid():
            topic = QuestionSubTopic.objects.get(id=topic_id)
            obj = qform.save(commit=False)
            obj.topic = topic
            obj.save()

    tform = TimeRecordForm
    qform = QuestionRecordForm
    
    progress = QuestionMainTopic.objects.filter(user=request.user)
    tprogress = TimeMainTopic.objects.filter(user=request.user)
    report = []
    
    datas = QuestionRecord.objects.filter(topic__main_topic__user=request.user).order_by("date")
    for data in datas:
        if len(report) != 0:
            if data.date == report[-1].date:
                report[-1].question_count += data.question_count
            else:
                report.append(data)
        else:
            report.append(data)

    # Daily
    today = timezone.now()
    daily = 0
    daily_objs = datas.filter(date=today.date())
    for a in daily_objs:
        daily += a.question_count
    
    yesterday = today - datetime.timedelta(days=1)
    before_day = 0
    before_daily_objs = datas.filter(date=yesterday.date())
    for a in before_daily_objs:
        before_day += a.question_count
    
    if before_day != 0:
        daily_persent = int(daily*100/before_day) - 100
    else:
        daily_persent = 100
    
    # Weekly
    this_week = today + relativedelta(weekday=MO(-1))
    weekly = 0
    weekly_objs = datas.filter(date__range=[this_week, today+relativedelta(weekday=MO(+1))])
    for a in weekly_objs:
        weekly += a.question_count
    
    before_week = 0
    before_weekly_objs = datas.filter(date__range=[today + relativedelta(weekday=MO(-2)), today + relativedelta(weekday=MO(-1))])
    for a in before_weekly_objs:
        before_week += a.question_count    
    
    if before_week != 0:
        weekly_persent = int(weekly*100/before_week) - 100
    else:
        weekly_persent = 100
    
    
    # Monthly
    month_objs = datas.filter(date__month=today.month)
    monthly = 0
    for a in month_objs:
        monthly += a.question_count
    
    before_month_value = today - relativedelta(months=1)
    before_month = 0
    before_monthly_objs = datas.filter(date__month=before_month_value.month)
    for a in before_monthly_objs:
        before_month += a.question_count
    
    if before_month != 0:
        monthly_persent = int(monthly*100/before_month) - 100
    else:
        monthly_persent = 100
    
    # Total
    total = 0
    total_left = 0
    total_persent = 0
    
    for a in progress:
        total += a.complated
    
    for b in progress:
        if b.target != 0 and type(b.target) == type(0):
            if b.target >= b.complated:
                total_left += (b.target-b.complated)
    
    if total != 0:
        total_persent = int(total*100/(total+total_left))
    

    context = {
        "qform": qform,
        "tform": tform,
        "sidebar_topic":progress,
        "ttopics":tprogress,
        "qtopics":progress,
        "progress":progress,
        "report":report,
        "label_name": "Tüm Dersler",
        
        # infobox
        "daily":daily,
        "daily_avg":before_day,
        "daily_persent":daily_persent,
        
        "weekly":weekly,
        "weekly_avg":before_week,
        "weekly_persent":weekly_persent,
        
        
        "monthly":monthly,
        "monthly_avg":before_month,
        "monthly_persent":monthly_persent,
        
        "total":total,
        "total_left": total_left,
        "total_persent":total_persent,
    }
    return render(request, 'pages/index.html', context)


@login_required
def sub_index(request, pk):
    if request.method == "POST":
        tform = TimeRecordForm(request.POST)
        qform = QuestionRecordForm(request.POST)
        topic_id = int(request.POST["sub_topic"])
        if tform.is_valid():
            topic = TimeSubTopic.objects.get(id=topic_id)
            obj = tform.save(commit=False)
            obj.topic = topic
            obj.save()
        if qform.is_valid():
            topic = QuestionSubTopic.objects.get(id=topic_id)
            obj = qform.save(commit=False)
            obj.topic = topic
            obj.save()

    tform = TimeRecordForm
    qform = QuestionRecordForm

    sidebar_topic = TimeMainTopic.objects.filter(user=request.user)
    progress = QuestionMainTopic.objects.filter(user=request.user, id=pk)
    tprogress = TimeMainTopic.objects.filter(user=request.user)
    qprogress = QuestionMainTopic.objects.filter(user=request.user)
    report = []
    
    datas = QuestionRecord.objects.filter(topic__main_topic__id=pk, topic__main_topic__user=request.user).order_by("date")
    for data in datas:
        if len(report) != 0:
            if data.date == report[-1].date:
                report[-1].question_count += data.question_count
            else:
                report.append(data)
        else:
            report.append(data)

    # Daily
    today = timezone.now()
    daily = 0
    daily_objs = datas.filter(date=today.date())
    for a in daily_objs:
        daily += a.question_count
    
    yesterday = today - datetime.timedelta(days=1)
    before_day = 0
    before_daily_objs = datas.filter(date=yesterday.date())
    for a in before_daily_objs:
        before_day += a.question_count
    
    if before_day != 0:
        daily_persent = int(daily*100/before_day) - 100
    else:
        daily_persent = 100
    
    # Weekly
    this_week = today + relativedelta(weekday=MO(-1))
    weekly = 0
    weekly_objs = datas.filter(date__range=[this_week, today+relativedelta(weekday=MO(+1))])
    for a in weekly_objs:
        weekly += a.question_count
    
    before_week = 0
    before_weekly_objs = datas.filter(date__range=[today + relativedelta(weekday=MO(-2)), today + relativedelta(weekday=MO(-1))])
    for a in before_weekly_objs:
        before_week += a.question_count    
    
    if before_week != 0:
        weekly_persent = int(weekly*100/before_week) - 100
    else:
        weekly_persent = 100
    
    
    # Monthly
    month_objs = datas.filter(date__month=today.month)
    monthly = 0
    for a in month_objs:
        monthly += a.question_count
    
    before_month_value = today - relativedelta(months=1)
    before_month = 0
    before_monthly_objs = datas.filter(date__month=before_month_value.month)
    for a in before_monthly_objs:
        before_month += a.question_count
    
    if before_month != 0:
        monthly_persent = int(monthly*100/before_month) - 100
    else:
        monthly_persent = 100
    
    # Total
    total = 0
    total_left = 0
    total_persent = 0
    
    for a in progress:
        total += a.complated
    
    for b in progress:
        if b.target != 0 and type(b.target) == int:
            if b.target >= b.complated:
                total_left += (b.target-b.complated)
    
    if total != 0:
        total_persent = int(total*100/(total+total_left))
    

    context = {
        "qform": qform,
        "tform": tform,
        "sidebar_topic":sidebar_topic,
        "ttopics":tprogress,
        "qtopics":qprogress,
        "progress":progress.first().question_main.all(),
        "report":report,
        "label_name": progress.first().name,
        
        # infobox
        "daily":daily,
        "daily_avg":before_day,
        "daily_persent":daily_persent,
        
        "weekly":weekly,
        "weekly_avg":before_week,
        "weekly_persent":weekly_persent,
        
        
        "monthly":monthly,
        "monthly_avg":before_month,
        "monthly_persent":monthly_persent,
        
        "total":total,
        "total_left": total_left,
        "total_persent":total_persent,
    }
    return render(request, 'pages/index.html', context)


def get_sub_topic(request):
    main_topic_id = request.GET.get("main_topic_id")
    sub_topics = QuestionSubTopic.objects.filter(main_topic=main_topic_id)
    context = {
        "sub_topics":list(sub_topics.values_list("id","sub_topic__name")),
    }
    return JsonResponse(context)


def update_target(request):
    if request.method == "POST":
        for obj in request.POST:
            if obj == "csrfmiddlewaretoken":
                continue
            main_topic = QuestionMainTopic.objects.filter(user=request.user, main_topic__name=obj)
            main_topic.update(target=int(request.POST[obj]))
    
    return redirect("qmain_topic")