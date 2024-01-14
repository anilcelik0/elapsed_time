from django.contrib import admin
from django.urls import path

from .views import index, sub_index

urlpatterns = [
    path("", index, name="main_topic"),
    path("sub/<int:pk>", sub_index, name="sub_topic")
]

