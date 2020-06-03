from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm
# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='recipe_list')

    return render(request, "recipes/home.html")


@login_required
def recipe_list(request):
    your_recipes = request.user.recipes.all()

    return render(request, "recipes/recipe_list.html",
                  {"recipes": your_recipes})


@login_required
def recipe_detail(request, recipe_pk):
    recipe = get_object_or_404(request.user.recipes, pk=recipe_pk)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect(to='recipe_detail', recipe_pk=recipe.pk)
    else:
        form = RecipeForm()

    return render(request, "recipes/add_recipe.html", {"form": form})


@login_required
def add_ingredient(request, recipe_pk):
    recipe = get_object_or_404(request.user.recipes, pk=recipe_pk)

    if request.method == "POST":
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect(to='recipe_detail', recipe_pk=recipe.pk)
    else:
        form = IngredientForm()

    return render(request, "recipes/add_ingredient.html", {
        "form": form,
        "recipe": recipe
    })
