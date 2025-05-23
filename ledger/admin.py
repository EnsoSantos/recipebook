from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1
    fields = ('image', 'description')

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', 'author__username')
    list_display = ('name', 'author', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    inlines = [RecipeIngredientInline, RecipeImageInline]

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
