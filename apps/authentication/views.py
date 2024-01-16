from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import SignUpForm, LoginForm, MyPasswordChangeForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class UserProfileView(FormView):
    template_name = 'pages/profile.html'
    form_class = UserUpdateForm
    # success_url = reverse_lazy('auth:profile')
  
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()

        initial['username'] = self.request.user.username
        initial['email'] = self.request.user.email
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name

        return initial


class AuthSignupView(FormView):
    template_name = 'pages/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AuthSigninView(FormView):
    template_name = 'pages/sign-in.html'
    form_class = LoginForm
    success_url = reverse_lazy("main_topic")


    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return super().post(request, *args, **kwargs)
        
        else:
            # return HttpResponseRedirect(reverse_lazy('auth:signin'))
            messages.add_message(request, messages.ERROR, "Login Failed")
            return HttpResponseRedirect(reverse_lazy('login'))

        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))
