from django.contrib import admin
from django.urls import path

from .views import index, sub_index, get_sub_topic, update_target

urlpatterns = [
    path("", index, name="qmain_topic"),
    path("sub/<int:pk>", sub_index, name="qsub_topic"),
    path("sub/get-topic/", get_sub_topic, name="question_get_sub_topic"),
    path("update-target/", update_target, name="qupdate_target")
]

