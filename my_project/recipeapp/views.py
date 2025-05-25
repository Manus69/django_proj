from django.shortcuts import render
from .models import Recipe

# Create your views here.
def rec_index(request):
    context = {
        "recs" : Recipe.objects.all()
    }

    return render(request, "recipeapp/index.html", context)

def rec_view(request):
    pass