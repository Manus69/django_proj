from django.urls import path
from .views import rec_index

app_name = "recipeapp"

urlpatterns = [
    path("", rec_index, name = "index")
]