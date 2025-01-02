from django.shortcuts import render, redirect
from .models import Item, Category
from django.shortcuts import get_object_or_404
from item.forms import AddItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def search_items_view(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category_id", "")

    
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    
    if query:
        items = items.filter(Q(name__icontains=query) |
                             Q(description__icontains=query))

    if category_id:
        category = Category.objects.get(id=category_id)
        items = category.items.all()

    context = {
        "items": items,
        "query": query,
        "categories": categories
    }
    return render(request, "item/search_items.html", context)


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)

    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(id=id)

    context = {
        "item": item,
        "related_items": related_items
    }
    return render(request, "item/item_detail.html", context)


@login_required
def add_item_view(request):
    context = {
        "title": "Add Product"
    }

    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            messages.success(request, "Item has been added successfully.")

            return redirect("item:item_detail", id=item.id)

    else:
        form = AddItemForm()
        context["form"] = form

    return render(request, "item/form.html", context)


@login_required
def edit_item_view(request, item_id):
    context = {
        "title": "Edit Product"
    }

    item = get_object_or_404(Item, id=item_id, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            messages.success(request, "Item has been updated successfully.")
            return redirect("item:item_detail", id=item.id)

    form = EditItemForm(instance=item)
    context["form"] = form

    return render(request, "item/form.html", context)


@login_required
def delete_item_view(request, item_id):
    item = get_object_or_404(
        Item, id=item_id, is_sold=False, created_by=request.user)

    item.delete()
    messages.success(request, "Item has been deleted successfully.")

    return redirect("dashboard:dashboard_home")
