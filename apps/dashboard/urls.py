from django.urls import path
from .views import index, profile, sign_in, sign_up

urlpatterns = [
    path("", index, name="index"),
    path("profile", profile, name="profile"),
    path("sign-in", sign_in, name="sign_in"),
    path("sign-up", sign_up, name="sign_up"),
]