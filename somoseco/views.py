from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User, Post, Campaign


def index(request):
    return render(request, 'somoseco/index.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Password match check
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "somoseco/register.html", {
                "message": "Passwords don't match."
            })
        
        user = User.objects.create_user(username, password, email)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("somoseco:index"))
    else:
        return render(request, "somoseco/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("somoseco:index"))
        else:
            return render(request, "somoseco/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "somoseco/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("somoseco:index"))