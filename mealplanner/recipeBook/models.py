from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)

    @property
    def recipes(self):
        recipe_object = Recipe.objects.filter_by(ingredients = self.id)
        return recipe_object

    def __str__(self):
        return f'{self.name}, quantity: {self.quantity}'

class Recipe(models.Model): 
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")

    def __str__(self):
        return f'{self.name}'
    