from django.urls import path

from .views import index, sub_index, get_sub_topic, update_target

urlpatterns = [
    path("", index, name="tmain_topic"),
    path("sub/<int:pk>", sub_index, name="tsub_topic"),
    path("sub/get-topic/", get_sub_topic, name="time_get_sub_topic"),
    path("update-target/", update_target, name="tupdate_target")
]