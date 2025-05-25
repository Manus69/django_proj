from django.core.management import BaseCommand
from django.contrib.auth.models import User
from recipeapp.models import Recipe

class Command(BaseCommand):
    def handle(self, * args, ** kwargs):
        self.stdout.write("test")
        user = User.objects.get(username="user")
        rec = Recipe.objects.create(
            name = "test",
            desc = "test ?",
            alg = "do this",
            time = -1,
            img = None,
            auth = user,
        )

        
