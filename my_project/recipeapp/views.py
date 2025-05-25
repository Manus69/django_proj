from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rec_index(request):
    context = {
        "x" : -1,
    }
    return render(request, "recipeapp/index.html", context)