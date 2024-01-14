from django.http import HttpResponse
from django.shortcuts import render
from .models import QuestionMainTopic, QuestionRecord
import datetime
from django.utils import timezone 
from dateutil.relativedelta import relativedelta, SU
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def index(request):
    progress = QuestionMainTopic.objects.filter(user=request.user)
    report = []
    
    datas = QuestionRecord.objects.filter(topic__main_topic__user=request.user).order_by("created_date")
    for data in datas:
        if len(report) != 0:
            if data.created_date.date() == report[-1].created_date.date():
                report[-1].question_count += data.question_count
            else:
                report.append(data)
        else:
            report.append(data)

    # Daily
    today = timezone.now()
    daily = 0
    daily_objs = datas.filter(created_date__date=today.date())
    for a in daily_objs:
        daily += a.question_count
    
    yesterday = today - datetime.timedelta(days=1)
    before_day = 0
    before_daily_objs = datas.filter(created_date__date=yesterday.date())
    for a in before_daily_objs:
        before_day += a.question_count
    
    if before_day != 0:
        daily_persent = int(daily*100/before_day) - 100
    else:
        daily_persent = 100
    
    # Weekly
    this_week = today + relativedelta(weekday=SU(-1))
    weekly = 0
    weekly_objs = datas.filter(created_date__range=[this_week, today+relativedelta(weekday=SU(+1))])
    for a in weekly_objs:
        weekly += a.question_count
    
    before_week = 0
    before_weekly_objs = datas.filter(created_date__range=[today + relativedelta(weekday=SU(-2)), today + relativedelta(weekday=SU(-1))])
    for a in before_weekly_objs:
        before_week += a.question_count    
    
    if before_week != 0:
        weekly_persent = int(weekly*100/before_week) - 100
    else:
        weekly_persent = 100
    
    
    # Monthly
    month_objs = datas.filter(created_date__month=today.month)
    monthly = 0
    for a in month_objs:
        monthly += a.question_count
    
    before_month_value = today - relativedelta(months=1)
    before_month = 0
    before_monthly_objs = datas.filter(created_date__month=before_month_value.month)
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
        if b.target != 0:
            if b.target >= b.complated:
                total_left += (b.target-b.complated)
    
    if total != 0:
        total_persent = int(total*100/(total+total_left))
    

    context = {
        "progress":progress,
        "report":report,
        
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
    progress = QuestionMainTopic.objects.filter(user=request.user, id=pk)
    report = []
    
    datas = QuestionRecord.objects.filter(topic__main_topic__id=pk, topic__main_topic__user=request.user).order_by("created_date")
    for data in datas:
        if len(report) != 0:
            if data.created_date.date() == report[-1].created_date.date():
                report[-1].question_count += data.question_count
            else:
                report.append(data)
        else:
            report.append(data)

    # Daily
    today = timezone.now()
    daily = 0
    daily_objs = datas.filter(created_date__date=today.date())
    for a in daily_objs:
        daily += a.question_count
    
    yesterday = today - datetime.timedelta(days=1)
    before_day = 0
    before_daily_objs = datas.filter(created_date__date=yesterday.date())
    for a in before_daily_objs:
        before_day += a.question_count
    
    if before_day != 0:
        daily_persent = int(daily*100/before_day) - 100
    else:
        daily_persent = 100
    
    # Weekly
    this_week = today + relativedelta(weekday=SU(-1))
    weekly = 0
    weekly_objs = datas.filter(created_date__range=[this_week, today+relativedelta(weekday=SU(+1))])
    for a in weekly_objs:
        weekly += a.question_count
    
    before_week = 0
    before_weekly_objs = datas.filter(created_date__range=[today + relativedelta(weekday=SU(-2)), today + relativedelta(weekday=SU(-1))])
    for a in before_weekly_objs:
        before_week += a.question_count    
    
    if before_week != 0:
        weekly_persent = int(weekly*100/before_week) - 100
    else:
        weekly_persent = 100
    
    
    # Monthly
    month_objs = datas.filter(created_date__month=today.month)
    monthly = 0
    for a in month_objs:
        monthly += a.question_count
    
    before_month_value = today - relativedelta(months=1)
    before_month = 0
    before_monthly_objs = datas.filter(created_date__month=before_month_value.month)
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
        if b.target != 0:
            if b.target >= b.complated:
                total_left += (b.target-b.complated)
    
    if total != 0:
        total_persent = int(total*100/(total+total_left))
    

    context = {
        "progress":progress.first().question_main.all(),
        "report":report,
        
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