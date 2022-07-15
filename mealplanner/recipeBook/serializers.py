from rest_framework import serializers
from rest_framework.reverse import reverse 
from .models import Recipe, Ingredient

class IngredientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            "name",
            "quantity",
        ]

class RecipeListSerializer(serializers.ModelSerializer):
    ingredients = IngredientDetailSerializer(many=True, read_only=True)
    # absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "ingredients", 
            # "absolute_url",
        ]

    # def get_absolute_url(self, obj):
    #     return reverse('recipe_detail', args=(obj.pk,))


class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientDetailSerializer(many=True, read_only=True)

    class Meta: 
        fields = [
            "id",
            "name",
            "ingredients", 
            # "absolute_url",
        ]
