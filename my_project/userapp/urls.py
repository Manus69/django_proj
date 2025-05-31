from django.shortcuts import redirect
from django.urls import path
from .views import profile_view, user_view
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .views import register


app_name = "userapp"


def my_logout(request):
    logout(request)
    return redirect("/")

urlpatterns = [
    path("profile/", profile_view, name="profile"),
    path("login/", LoginView.as_view(template_name="userapp/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", my_logout, name="logout"),
    path("register/", register, name="register"),
    path("<str:name>/", user_view, name="user")
]