from django.http import HttpResponse
from django.shortcuts import render
from .models import QuestionMainTopic

# Create your views here.

def index(request):
    progress = QuestionMainTopic.objects.filter(user=request.user)
    colors = progress.values_list('color')
    
    context = {
        "progress":progress,
        "colors": colors,
    }
    return render(request, 'pages/index.html', context)