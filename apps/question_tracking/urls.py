from django.contrib import admin
from django.urls import path

from .views import index, sub_index, get_sub_topic, update_target

urlpatterns = [
    path("", index, name="main_topic"),
    path("sub/<int:pk>", sub_index, name="sub_topic"),
    path("sub/get-topic/", get_sub_topic, name="get_sub_topic"),
    path("update-target/", update_target, name="update_target")
]

