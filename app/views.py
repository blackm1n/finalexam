from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import RegisterForm, LoginForm, LogoutForm, RecipeForm
from .models import Recipe
from random import sample

def main(request):
    logged_in = True if request.user.is_authenticated else False
    recipes = sample(list(Recipe.objects.all()), 5)
    context = {'logged_in': logged_in, 'recipes1': recipes[:3], 'recipes2': recipes[3:]}
    if logged_in:
        context['user'] = request.user
    return render(request, "app/main.html", context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('main')
    else:
        form = RegisterForm()
        return render(request, 'app/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('main')
            else:
                message = 'Введенные имя пользователя или пароль неверны'
                return render(request, 'app/login.html', {'form': form, 'error': True, 'message': message})
    else:
        form = LoginForm()
        return render(request, 'app/login.html', {'form': form, 'error': False})


def logout(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = LogoutForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['confirm']:
                    auth_logout(request)
                    return redirect('main')
        else:
            form = LogoutForm()
            return render(request, 'app/logout.html', {'form': form, 'logged_in': True, 'user': request.user})
    else:
        return redirect('main')


def create_recipe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                steps = form.cleaned_data['steps']
                cook_time = form.cleaned_data['cook_time']
                image = form.cleaned_data['image']
                recipe = Recipe(title=title, description=description, steps=steps, cook_time=cook_time, author=request.user, image=image)
                recipe.save()
                return redirect('main')
        else:
            form = RecipeForm()
            return render(request, 'app/create_recipe.html', {'form': form, 'logged_in': True, 'user': request.user})
    else:
        return redirect('main')


def all_recipes(request, page):
    logged_in = True if request.user.is_authenticated else False
    recipes = list(Recipe.objects.all())[(page - 1) * 9 : page * 9]
    context = {'logged_in': logged_in, 'recipes': recipes, 'page_number': page, 'last_page': page - 1, 'next_page': page + 1}
    if logged_in:
        context['user'] = request.user
    return render(request, "app/all_recipes.html", context)

def recipe(request, id):
    logged_in = True if request.user.is_authenticated else False
    recipe = Recipe.objects.filter(pk=id).first()
    context = {'logged_in': logged_in, 'recipe': recipe}
    if logged_in:
        context['user'] = request.user
    return render(request, "app/recipe.html", context)

def your_recipes(request, page):
    if request.user.is_authenticated:
        recipes = list(Recipe.objects.filter(author_id=request.user.id))[(page - 1) * 9 : page * 9]
        context = {'logged_in': True, 'user': request.user, 'recipes': recipes, 'page_number': page, 'last_page': page - 1, 'next_page': page + 1}
        return render(request, "app/your_recipes.html", context)
    else:
        return redirect('main')

def edit_recipe(request, id):
    if request.user.is_authenticated:
        recipe = Recipe.objects.filter(pk=id).first()
        if request.method == "POST":
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                steps = form.cleaned_data['steps']
                cook_time = form.cleaned_data['cook_time']
                image = form.cleaned_data['image']
                recipe.title = title
                recipe.description = description
                recipe.steps = steps
                recipe.cook_time = cook_time
                if image:
                    recipe.image = image
                recipe.save()
                return redirect('main')
        else:
            form = RecipeForm(initial={'title': recipe.title, 'description': recipe.description, 'steps': recipe.steps, 'cook_time': recipe.cook_time, 'image': recipe.image})
            return render(request, 'app/edit_recipe.html', {'form': form, 'logged_in': True, 'user': request.user})
    else:
        return redirect('main')