from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, ContactForm
from .models import *


def homepage(request):
    return render(request, 'spicyo/index.html')


# def post(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     form = ContactForm()
#     if request.method == 'POST':
#         form = form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     ctx = {"form": form}
#     return render(request, 'spicyo/footer.html', ctx)



def about(request):
    return render(request, 'spicyo/about.html')


def recipe(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'spicyo/recipe.html', ctx)


def blog(request):
    return render(request, 'spicyo/blog.html')


def contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm()
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    ctx = {"form": form}
    return render(request, 'spicyo/index.html', ctx)
