from django.db import models

# Create your models here.
class Recipe(models.Model): 
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    recipes = models.ManyToManyField(Recipe, related_name="ingredients")

    def __str__(self):
        return f'{self.name}, quantity: {self.quantity}'

