from django.urls import path
from .views import recipes_list, recipe_detail, recipe_create, recipe_image
from . import views

urlpatterns = [
    path('', recipes_list, name='recipes_list'),
    path('recipes/list/', recipes_list, name="recipes_list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe_detail"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recipe/add/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/add_image', views.recipe_image, name='recipe_image'),
]


app_name = 'ledger'