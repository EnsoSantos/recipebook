from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self) :
        return reverse('ingredient_detail', args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
        
    def get_absolute_url(self) :
        return reverse('ledger:recipe_detail', args=[self.pk])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100) 
    ingredient = models.ForeignKey(Ingredient, null=True, on_delete=models.SET_NULL, related_name='recipe_ingredients')
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL, related_name='ingredients')

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} in {self.recipe.name}"