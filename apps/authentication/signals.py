from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.question_tracking.models import QuestionMainTopic
from apps.models import MainTopic

@receiver(post_save, sender=User)
def create_main_topic(sender, instance, created, **kwargs):
    if created:
        topics = MainTopic.objects.all()
        for topic in topics:
            QuestionMainTopic.objects.create(user=instance, main_topic=topic)