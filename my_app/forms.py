# # yourapp/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# # from django.contrib.auth.models import User
# from .models.user import User

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email address...'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
#         }

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}))

#     class Meta:
#         model = User
#         fields = ('username', 'password')





from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models.user import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email address...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}))
