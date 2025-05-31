from django.urls import path
from .views import rec_index, rec_create, rec_view, rec_update

app_name = "recipeapp"

urlpatterns = [
    path("", rec_index, name="index"),
    path("create/", rec_create, name="create"),
    path("update/<int:pk>", rec_update, name="update"),
    path("<int:_pk>", rec_view, name="recipe"),
]