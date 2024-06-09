from django.urls import path
from . import views

app_name = 'somoseco'  # Define the namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
]