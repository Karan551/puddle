from django.shortcuts import render
from .models import Item
from django.shortcuts import get_object_or_404

# Create your views here.


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)

    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(id=id)

    context = {
        "item": item,
        "related_items": related_items
    }
    return render(request, "item/item_detail.html", context)
