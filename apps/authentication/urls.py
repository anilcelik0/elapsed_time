from django.urls import path
from .views import AuthSigninView, AuthSignupView, logout_view, UserProfileView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', AuthSigninView.as_view(template_name = 'pages/auth/signin.html'), name='signin'),
    path('logout/', logout_view, name='logout'),
    path('signup', AuthSignupView.as_view(template_name = 'pages/auth/signup.html'), name='signup'),
]

