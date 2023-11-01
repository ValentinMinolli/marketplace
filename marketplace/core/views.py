from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from item.models import Category, Item

from .forms import SignUpForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
        },
    )


def contact(request):
    return render(request, "core/contact.html")


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})


def about(request):
    return render(request, "core/about.html")
