from django.db import models

# Create your models here.
class Recipe(models.Model): 
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe, related_name="recipes")

    def __str__(self):
        return f'{self.name}'

