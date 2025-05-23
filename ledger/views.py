from django.shortcuts import render, redirect
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RecipeForm

@login_required
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
    images = recipe.images.all()
    ctx = {
        "recipe": recipe,
        "recipe_ingredients": recipe_ingredients,
        "images": images,
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
            return HttpResponseRedirect(reverse("ledger:recipes_list"))
    
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("ledger:recipes_list"))
        else:
            error = "Incorrect password for existing user."
    return render(request, "ledger/login.html", {"error": error})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def recipe_create(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.profile
            recipe.save()
            return redirect('ledger:recipe_detail', pk=recipe.id)
    else:
        recipe_form = RecipeForm()

    ctx = {
        'recipe_form': recipe_form,
    }

    return render(request, 'ledger/recipe_form.html', ctx)


