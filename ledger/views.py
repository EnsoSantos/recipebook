from django.shortcuts import render
from .models import Recipe, Ingredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "ledger/recipe_list.html", ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()
    ctx = {
        "recipe": recipe,
        "ingredients": ingredients
    }
    return render(request, "ledger/recipe_detail.html", ctx)