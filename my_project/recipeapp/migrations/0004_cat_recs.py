# Generated by Django 5.1.7 on 2025-05-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0003_recipe_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='recs',
            field=models.ManyToManyField(related_name='category', to='recipeapp.recipe'),
        ),
    ]
