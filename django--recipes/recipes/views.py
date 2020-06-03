from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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
