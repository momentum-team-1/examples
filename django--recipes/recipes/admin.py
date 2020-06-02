from django.contrib import admin
from .models import Recipe, Ingredient, RecipeStep, Tag
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeStep)
admin.site.register(Tag)
