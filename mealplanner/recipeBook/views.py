from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import IngredientDetailSerializer, RecipeListSerializer, RecipeDetailSerializer
from .models import Recipe, Ingredient

# Create your views here.

# READ VIEWS
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

# CREATE VIEWS 
class RecipeCreateAPIView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer

class IngredientCreateAPIView(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer

# UPDATE VIEWS 
class RecipeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer

class IngredientRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Ingredient.objects.all() 
    serializer_class = IngredientDetailSerializer


# EXPERIMENT WITH CREATE 
class RecipeCreateSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer

    def get_queryset(self):
        recipe = Recipe.objects.all()
        return recipe 

    def create(self, request, *args, **kwargs):
        data = request.data 

        new_recipe = Recipe.objects.create(name=data["name"])
        new_recipe.save() 

        if "ingredients" in data:
            for ingredient in data['ingredients']:
                ing_obj = Ingredient.objects.get(name = ingredient['name'])
                if not ing_obj.exists():
                    ingredient_obj = Ingredient.objects.create(name = ingredient["name"],
                                                                quantity = ingredient["quantity"])
                    ingredient_obj.save()
                    ing_obj = Ingredient.objects.get(name = ingredient['name'])
                new_recipe.ingredients.add(ing_obj)

        serializer = RecipeDetailSerializer(new_recipe)

        return Response(serializer.data)

class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientDetailSerializer

    def get_queryset(self):
        ingredient = Ingredient.objects.all()
        return ingredient