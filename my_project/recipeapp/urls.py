from django.urls import path
from .views import rec_index, rec_create, rec_view

app_name = "recipeapp"

urlpatterns = [
    path("", rec_index, name="index"),
    path("create/", rec_create, name="create"),
    path("<int:_pk>", rec_view, name="recipe"),
]