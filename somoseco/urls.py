from django.urls import path
from . import views

app_name = 'somoseco'  # Define the namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>', views.profile_view, name='profile'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
]