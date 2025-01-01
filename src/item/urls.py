from django.urls import path
from . import views

app_name="item"

urlpatterns = [
    path("item-detail/<int:id>", views.item_detail, name="item_detail"),
]
