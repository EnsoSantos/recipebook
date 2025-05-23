from django.shortcuts import render
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    ctx = {
        "recipe": recipe,
        "recipe_ingredients": recipe_ingredients
    }
    return render(request, "ledger/recipe_detail.html", ctx)


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("recipes_list"))
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("recipes_list"))
        else:
            error = "Incorrect password for existing user."

    return render(request, "ledger/login.html", {"error": error})