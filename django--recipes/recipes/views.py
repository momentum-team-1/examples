from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tag, Recipe
from .forms import RecipeForm, IngredientForm, RecipeStepForm
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
    recipe = get_object_or_404(Recipe.objects.filter(user=request.user), pk=recipe_pk)
    ingredient_form = IngredientForm()
    return render(request, "recipes/recipe_detail.html", {
        "recipe": recipe,
        "ingredient_form": ingredient_form,
    })


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            recipe.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='recipe_detail', recipe_pk=recipe.pk)
    else:
        form = RecipeForm()

    return render(request, "recipes/add_recipe.html", {"form": form})


@login_required
def edit_recipe(request, recipe_pk):
    recipe = get_object_or_404(request.user.recipes, pk=recipe_pk)

    if request.method == "POST":
        form = RecipeForm(instance=recipe, data=request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='recipe_detail', recipe_pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe, initial={"tag_names": recipe.get_tag_names()})

    return render(request, "recipes/edit_recipe.html", {
        "form": form,
        "recipe": recipe
    })


@login_required
def delete_recipe(request, recipe_pk):
    recipe = get_object_or_404(request.user.recipes, pk=recipe_pk)

    if request.method == "POST":
        recipe.delete()
        return redirect(to='recipe_list')

    return render(request, "recipes/delete_recipe.html", { "recipe": recipe })


@login_required
def add_ingredient(request, recipe_pk):
    recipe = get_object_or_404(request.user.recipes, pk=recipe_pk)

    if request.method == "POST":  # submitted the form
        form = IngredientForm(data=request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect(to='recipe_detail', recipe_pk=recipe.pk)
    else:  # viewing page for first time
        form = IngredientForm()

    return render(request, "recipes/add_ingredient.html", {
        "form": form,
        "recipe": recipe
    })


@login_required
def add_recipe_step(request, recipe_pk):
    recipe = get_object_or_404(request.user.recipes, pk=recipe_pk)

    if request.method == "POST":  # submitted the form
        form = RecipeStepForm(data=request.POST)
        if form.is_valid():
            recipe_step = form.save(commit=False)
            recipe_step.recipe = recipe
            recipe_step.save()
            return redirect(to='recipe_detail', recipe_pk=recipe.pk)
    else:
        form = RecipeStepForm()

    return render(request, "recipes/add_recipe_step.html", {
        "form": form,
        "recipe": recipe
    })

@login_required
def view_tag(request, tag_name):
    """
    Given a tag name, look up the tag and then get all recipes for the
    current user with that tag.
    """
    tag = get_object_or_404(Tag, tag=tag_name)
    recipes = tag.recipes.filter(user=request.user)
    return render(request, "recipes/tag_detail.html", {"tag": tag, "recipes": recipes})
