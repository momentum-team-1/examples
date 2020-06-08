from django import forms
from .models import Recipe, Ingredient, RecipeStep


class RecipeForm(forms.ModelForm):
    tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput(attrs={'class': 'pa2 f4 w-100'}))

    class Meta:
        model = Recipe
        fields = [
            'title',
            'prep_time_in_minutes',
            'cook_time_in_minutes',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'pa2 f4 w-100'}),
            'prep_time_in_minutes': forms.NumberInput(attrs={'class': 'pa2 f4 w-100'}),
            'cook_time_in_minutes': forms.NumberInput(attrs={'class': 'pa2 f4 w-100'})
        }


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
