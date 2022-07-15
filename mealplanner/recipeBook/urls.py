from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.RecipeListAPIView.as_view(), name='recipe_list'),
    path('ingredient/<int:id>/', views.IngredientDetailAPIView.as_view(), name='ingredient_detail'),
    path('recipe/<int:id>/', views.RecipeDetailAPIView.as_view(), name='recipe_detail'), 
    
]