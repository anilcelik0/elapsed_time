from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    
    def clean_email(self):
        """Reject email that differ only in case."""
        username = self.cleaned_data.get("email")
        if (
            username
            and self._meta.model.objects.filter(email__iexact=username).exists()
        ):
            self._update_errors(
                forms.ValidationError(
                    {
                        "email": self.instance.unique_error_message(
                            self._meta.model, ["email"]
                        )
                    }
                )
            )
        else:
            return username


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
    


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

class MyPasswordChangeForm(forms.Form):
    old_password = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        ))
    
    new_password1 = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        ))
    
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ))
