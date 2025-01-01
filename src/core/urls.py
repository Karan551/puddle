from django.urls import path
from . import views


app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("contact/", views.contact, name="contact"),
]
