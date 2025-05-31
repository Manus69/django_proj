from django import forms
from .models import CF_LEN_MAX, Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "name", "desc", "alg", "time", "img"



# class RecipeForm(forms.Form):
#     name = forms.CharField(label="Name ", max_length=CF_LEN_MAX)
#     desc = forms.CharField(label="Description ", widget=forms.Textarea)
#     alg = forms.CharField(label="Algorithm ", widget=forms.Textarea)
#     time = forms.IntegerField(label="Cooking time ", min_value=1, max_value=69, initial=1)