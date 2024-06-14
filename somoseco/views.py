from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

from .models import User, Post, Campaign


def index(request):
    return render(request, 'somoseco/index.html')


def profile_view(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'somoseco/profile.html', {
        'user': user
    })

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    allPosts = Post.objects.filter(user=user).order_by("id").reverse()
    
    #Paginator
    p = Paginator(allPosts, 2)
    pageNumber = request.GET.get('page')
    posts_of_page = p.get_page(pageNumber)
    return render(request, "network/profile.html", {
        "allPosts": allPosts,
        "posts_of_page": posts_of_page,
        "username": user.username,
        "user_profile": user,
    })

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["name"]

        # Password match check
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "somoseco/signup.html", {
                "message": "Passwords don't match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "somoseco/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("somoseco:index"))
    else:
        return render(request, "somoseco/signup.html")


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