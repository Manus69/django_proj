from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_view(request):
    return render(request, "userapp/profile.html", {"user" : request.user})

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "userapp/register.html"
    success_url = reverse_lazy("userapp:profile")