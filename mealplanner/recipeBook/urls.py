from django.urls import path 
from django.conf.urls import include 
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('experiment-create', views.RecipeCreateSet, basename='experiment-create')

urlpatterns = [
    path('', views.RecipeListAPIView.as_view(), name='recipe_list'),
    path('ingredients', views.IngredientListAPIView.as_view(), name='ingredient_list'),
    path('ingredient/<int:id>/', views.IngredientDetailAPIView.as_view(), name='ingredient_detail'),
    path('recipe/<int:id>/', views.RecipeDetailAPIView.as_view(), name='recipe_detail'), 
    path('create_recipe/', views.RecipeCreateAPIView.as_view(), name='recipe_create'),
    path('update_recipe/<int:id>/', views.RecipeRetrieveUpdateAPIView.as_view(), name='recipe_update'),
    path('create_ingredient/', views.IngredientCreateAPIView.as_view(), name='ingredient_create'),
    path('update_ingredient/<int:id>/', views.IngredientRetrieveUpdateAPIView.as_view(), name='ingredient_update'),
    path('destroy_recipe/<int:id>/', views.RecipeDestroyAPIView.as_view(), name='destroy_recipe'),
    path('destroy_ingredient/<int:id>/', views.IngredientDestroyAPIView.as_view(), name='destroy_ingredient'),
    path('',include(router.urls))
]