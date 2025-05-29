from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def profile_view(request):
    return render(request, "userapp/profile.html", {"user" : request.user})

def user_view(request, name):
    if name == request.user.username:
        return profile_view(request)
    
    print(name, request.user.username)
    user = get_object_or_404(User, username=name)
    
    return render(request, "userapp/user.html", { "user" : user })

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "userapp/register.html"
    success_url = reverse_lazy("userapp:profile")