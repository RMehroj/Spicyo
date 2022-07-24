from django.shortcuts import render, redirect
from .models import *


def homepage(request):
    return render(request, 'spicyo/index.html')


def post(request, pk):
    contacts = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact = Contact(request.POST, isinstance=contacts)
        if contact.is_valid():
            contact.save()
            return redirect('/')
        ctx = {"contact": contact}
        return render(request, 'spicyo/index.html', ctx)



def about(request):
    return render(request, 'spicyo/about.html')


def recipe(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'spicyo/recipe.html', ctx)


def blog(request):
    return render(request, 'spicyo/blog.html')


def contact(request):
    return render(request, 'spicyo/contact.html')
