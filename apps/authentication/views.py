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

class UserProfileView(TemplateView):
    template_name = 'pages/profile.html'
    # form_class = UserProfileForm
    # success_url = reverse_lazy('auth:profile')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        user_update_form = UserUpdateForm
        change_password_form = MyPasswordChangeForm
        # Define the layout for this module
        # _templates/layout/auth.html
        context.update({
            'user_update_form': user_update_form,
            'change_password_form':change_password_form
        })

        return context

    
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            user = request.user
            user_object = User.objects.get(id=user.id)
            
            user_update_form  = UserUpdateForm(request.POST)
            change_password_form = MyPasswordChangeForm(request.POST)

            user_updatet_valid = user_update_form.is_valid()
            change_password_valid = change_password_form.is_valid()
            
            if "user_update" in request.POST:
                user_object.username = user_update_form["username"].value()
                user_object.email = user_update_form["email"].value()
                user_object.first_name = user_update_form["first_name"].value()
                user_object.last_name = user_update_form["last_name"].value()
                user_object.save()
                messages.add_message(request, messages.SUCCESS, 'user successfuly updated')
                
            elif "change_password" in request.POST:
                currentpassword = request.user.password

                old_password = change_password_form["old_password"].value()
                password1 = change_password_form["new_password1"].value()
                password2 = change_password_form["new_password2"].value()

                matchcheck= check_password(old_password, currentpassword)

                if matchcheck:
                    if password1 == password2:
                        user_object.set_password(password1)
                        user_object.save()
                        messages.add_message(request, messages.SUCCESS, 'password successfuly changed')
                    
                    else:
                        messages.add_message(request, messages.ERROR, 'passwords not match')
                        
                else:
                    messages.add_message(request, messages.ERROR, 'incorrect passwords ')

        return render(request, self.template_name, self.get_context_data())
    

    def get_initial(self):
        initial = super().get_initial()

        initial['bio'] = self.request.user.username

        return initial


class AuthSignupView(FormView):
    template_name = 'pages/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('authentication:login')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AuthSigninView(FormView):
    template_name = 'pages/signin.html'
    form_class = LoginForm
    success_url = ""


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
            return HttpResponseRedirect(reverse_lazy('authentication:login'))

        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('authentication:login'))
