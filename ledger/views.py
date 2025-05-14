from django.shortcuts import render
from .models import Recipe, Ingredient

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = Ingredient.objects.filter(recipeingredient__recipe=recipe)
    ctx = {
        "recipe": recipe,
        "ingredients": ingredients
    }
    return render(request, "ledger/recipe_detail.html", ctx)