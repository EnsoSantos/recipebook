from django.urls import path
from .views import recipes_list, recipe_detail
from . import views

urlpatterns = [
    path('', recipes_list, name='recipes_list'),
    path('recipes/list/', recipes_list, name="recipes_list"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe_detail"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]


app_name = 'ledger'