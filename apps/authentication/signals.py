from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.question_tracking.models import QuestionMainTopic, QuestionSubTopic
from apps.models import MainTopic
from apps.time_tracking.models import TimeMainTopic, TimeSubTopic

@receiver(post_save, sender=User)
def create_main_topic(sender, instance, created, **kwargs):
    if created:
        topics = MainTopic.objects.all()
        for topic in topics:
            question = QuestionMainTopic.objects.create(user=instance, main_topic=topic)
            time = TimeMainTopic.objects.create(user=instance, main_topic=topic)
            
            for sub in topic.main_topic.all():
                QuestionSubTopic.objects.create(main_topic=question, sub_topic=sub)
                TimeSubTopic.objects.create(main_topic=time, sub_topic=sub)
                