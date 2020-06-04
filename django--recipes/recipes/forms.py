from django import forms
from .models import Recipe, Ingredient, RecipeStep


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'prep_time_in_minutes',
            'cook_time_in_minutes',
        ]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'amount',
            'item',
        ]


class RecipeStepForm(forms.ModelForm):
    class Meta:
        model = RecipeStep
        fields = ['text']
