from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
def rec_index(request):
    context = {
        "recs" : Recipe.objects.all()
    }

    return render(request, "recipeapp/index.html", context)

def rec_create(request):

    form = RecipeForm()
    if request.method == "POST":
        # Recipe.objects.all().delete()

        form = RecipeForm(request.POST)
        # 
        print(request.user)

        if form.is_valid():
            form.cleaned_data["auth"] = request.user
            
            # form.save()
            Recipe.objects.create(** form.cleaned_data)

            url = reverse("recipeapp:index")
            return redirect(url)
        else:
            print("????")
            print(form.errors.as_data())
    
    form = RecipeForm()
    context = {
        "form" : form
    }

    return render(request, "recipeapp/create.html", context=context)

def rec_view(request, _pk):
    rec = get_object_or_404(Recipe, pk=_pk)

    return render(request, "recipeapp/recipe.html", {"rec" : rec})
