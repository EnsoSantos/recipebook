from django.shortcuts import render
from .models import Recipe, RecipeIngredient

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    ctx = {
        "recipe": recipe,
        "recipe_ingredients": recipe_ingredients
    }
    return render(request, "ledger/recipe_detail.html", ctx)