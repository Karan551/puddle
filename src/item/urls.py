from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.search_items_view, name="search_item"),
    path("item-detail/<int:id>", views.item_detail, name="item_detail"),
    path("add-product/", views.add_item_view, name="add_item"),
    path("edit-product/<int:item_id>", views.edit_item_view, name="edit_item"),
    path("delete-product/<int:item_id>", views.delete_item_view, name="delete_item"),
]
