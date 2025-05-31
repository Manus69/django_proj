from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
import random
def rec_index(request):
    context = {
        "recs" : Recipe.objects.order_by('?')
        # "recs" : Recipe.objects.all()
    }

    return render(request, "recipeapp/index.html", context)

@login_required(login_url="userapp:login")
def rec_create(request):

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        form.instance.auth = request.user
        if form.is_valid():
            form.save()

            url = reverse("recipeapp:index")
            return redirect(url)
    
    form = RecipeForm()
    context = {
        "form" : form
    }

    return render(request, "recipeapp/create.html", context=context)

@login_required(login_url="userapp:login")
def rec_update(request, pk):
    inst = get_object_or_404(Recipe, id=pk)

    if inst.auth != request.user:
        return rec_view(request, pk)
    
    form = RecipeForm(request.POST or None, instance=inst)

    if form.is_valid():
        form.save()

        return redirect(reverse("recipeapp:index"))
    
    return render(request, "recipeapp/create.html", {"form" : form})

from django.contrib import messages

def rec_view(request, _pk):
    rec = get_object_or_404(Recipe, pk=_pk)

    messages.debug(request, f"Obj : {rec.name} {rec.auth} {rec.img}")
    return render(request, "recipeapp/recipe.html", {"rec" : rec})

