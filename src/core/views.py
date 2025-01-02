from django.shortcuts import render, redirect
from django.http import HttpResponse
from item.models import Category, Item
from core.forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, alogout
# Create your views here.


def index(request):

    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)[:6]

    context = {
        "categories": categories,
        "items": items,
        "title": "Newest"
    }

    return render(request, "core/index.html", context)


def catgories_prod_view(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    items = category.items.all()
    
    title = category.name[:-1] if category.name[-1] == "s" else category.name

    context = {
        "items": items,
        "title": title,
        "categories": categories
    }
    return render(request, "core/index.html", context)


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        print("form errors::", form.errors)

        if form.is_valid():

            form.save()
            messages.success(request, "Form saved successfully.")
            return redirect("/")

    else:
        form = SignupForm()
    return render(request, "core/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(request, "Login Successfully.")
            # redirect user
            return redirect("/")

    form = LoginForm()
    return render(request, "core/login.html", {"form": form})


def user_logout(request):
    if request.method == "POST":

        logout(request)
        messages.success(request, "Logout Successfully.")
        # redirect to home
        return redirect("/")


def contact(request):
    return render(request, "core/contact.html")
