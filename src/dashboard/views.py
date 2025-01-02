from django.shortcuts import render
from item.models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def dashoboard_home_view(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        "items": items
    }
    return render(request, "dashboard/dashboard_home.html", context)
