from django import forms
from .models import Recipe, RecipeIngredient, RecipeImage
from django.forms import inlineformset_factory


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author', 'created_on', 'updated_on']
        fields = ['name', ]

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description', ]

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=3,
    can_delete=False,
)


