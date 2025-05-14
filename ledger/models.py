from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100) 
    ingredient = models.ForeignKey(Ingredient, null=True, on_delete=models.SET_NULL, related_name='recipe_ingredients')
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL, related_name='ingredients')

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} in {self.recipe.name}"