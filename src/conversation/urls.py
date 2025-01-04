from django.urls import path
from . import views


app_name = "conversation"
urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("new/<int:item_id>", views.new_conversation_view, name="new"),
    path("<int:conversation_id>", views.conversation_detail_view, name="detail"),
]
