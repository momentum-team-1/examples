from django.db import models
from users.models import User


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


class Recipe(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='recipes')
    title = models.CharField(max_length=255)
    prep_time_in_minutes = models.PositiveIntegerField(null=True, blank=True)
    cook_time_in_minutes = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name="recipes")

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(to=Recipe,
                               on_delete=models.CASCADE,
                               related_name='ingredients')
    amount = models.CharField(max_length=20)
    item = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.amount} {self.item}"


class RecipeStep(models.Model):
    recipe = models.ForeignKey(to=Recipe,
                               on_delete=models.CASCADE,
                               related_name='steps')
    step_num = models.PositiveIntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.step_num} {self.text}"
