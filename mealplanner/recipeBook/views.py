from django.shortcuts import render
from rest_framework import generics
from .serializers import IngredientDetailSerializer, RecipeListSerializer, RecipeDetailSerializer
from .models import Recipe, Ingredient

# Create your views here.
class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer

class IngredientDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer

class RecipeDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer