from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(
        label="UserName :",

        help_text="Usernames may contain alphanumeric, _, @, +, . and - characters.",

        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your Username :",
                "autocomplete": "username",
                "class": "w-full px-4 py-2 rounded-xl text-lg md:text-xl outline-none focus:ring-1 focus:ring-indigo-600"
            }
        ))

    email = forms.EmailField(
        label="Email :",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter Your Email: ",
                "class": "w-full px-4 py-2 rounded-xl text-lg md:text-xl outline-none focus:ring-1 focus:ring-indigo-600"
            }
        ))

    password1 = forms.CharField(
        label="Password :",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Your Password: ",
                "autocomplete": "new-password",
                "class": "w-full px-4 py-2 rounded-xl text-lg md:text-xl outline-none focus:ring-1 focus:ring-indigo-600"
            }
        ))

    password2 = forms.CharField(
        label="Confirm Password :",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Your Password: ",
                "autocomplete": "new-password",
                "class": "w-full px-4 py-2 rounded-xl text-lg md:text-xl outline-none focus:ring-1 focus:ring-indigo-600"
            }
        ))


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField(
        label="UserName :",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Your Username :",
                "autocomplete": "username",
                "class": "w-full px-4 py-2 rounded-xl text-lg md:text-xl outline-none focus:ring-1 focus:ring-indigo-600"
            }
        ))

    password = forms.CharField(
        label="Password :",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Your Password: ",
                "autocomplete": "new-password",
                "class": "w-full px-4 py-2 rounded-xl text-lg md:text-xl outline-none focus:ring-1 focus:ring-indigo-600"
            }
        ))
