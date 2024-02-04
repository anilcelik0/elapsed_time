from django.db import models
from apps.models import BaseModel, MainTopic, SubTopic
from django.contrib.auth import get_user_model
from random import randint

# Create your models here.

def random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color_string = 'rgb('+str(r)+','+str(g)+','+str(b)+')'
    return rand_color_string


class TimeMainTopic(BaseModel):    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="time")
    main_topic = models.ForeignKey(MainTopic, on_delete=models.CASCADE, related_name="time_main_topic")
    color = models.CharField(max_length=20, null=True, blank=True)
    
    target = models.IntegerField(null=True, blank=True)
    target_is_complated = models.BooleanField(default=False)
    
    @property
    def complated(self):
        count = 0
        try:
            for records in self.time_main.all():
                for record in records.topic.all():
                    count += record.hour
            
            return count
        
        except:
            return count
    
    @property
    def total(self):
        if self.target:
            return self.target
        else:
            return 0
        
    @property
    def complated_percent(self):
        try:
            return int(self.complated*100/self.total)
        except:
            return 0
    
    @property
    def name(self):
        return self.main_topic.name
    
    def save(self, *args, **kwargs):
        self.color = random_rgb()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name


class TimeSubTopic(BaseModel):
    main_topic = models.ForeignKey(TimeMainTopic, on_delete=models.CASCADE, related_name="time_main")
    sub_topic = models.ForeignKey(SubTopic, null=True, blank=True, on_delete=models.CASCADE, related_name="time_sub")
    color = models.CharField(max_length=20, null=True, blank=True)
    
    @property
    def complated(self):
        count = 0
        try:
            for record in self.topic.all():
                count += record.hour
            
            return count
        
        except:
            return count
    
    @property
    def name(self):
        if self.sub_topic:
            return self.sub_topic.name
        else:
            return self.main_topic.name
    
    @property
    def complated_percent(self):
        try:
            return int(self.complated*100/self.main_topic.total)
        except:
            return 0
        
    def save(self, *args, **kwargs):
        self.color = random_rgb()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        if self.sub_topic:
            return self.sub_topic.name
        else:
            return self.main_topic.name


class TimeRecord(BaseModel):
    topic = models.ForeignKey(TimeSubTopic, on_delete=models.CASCADE, related_name="topic")
    hour = models.FloatField()
    date = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.topic.__str__()