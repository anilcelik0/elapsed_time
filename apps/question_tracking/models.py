from collections.abc import Iterable
from django.db import models
from apps.models import BaseModel, SubTopic

# Create your models here.


class Questions(BaseModel):
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.CASCADE, related_name="sub_topic")
    questions_count = models.IntegerField()
    correct_answer = models.IntegerField()
    wrong_answer = models.IntegerField()
    
