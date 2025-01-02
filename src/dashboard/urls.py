from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.dashoboard_home_view, name="dashboard_home")
]
