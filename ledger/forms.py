from django import forms
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author', 'created_on', 'updated_on']
        fields = ['name', ]

class RecipeImage(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description', ]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['quantity', 'ingredient', ]


