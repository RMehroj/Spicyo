from email import message
from tokenize import group

from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group

from .forms import ContactForm, CreateUserForm, RecipeForm
from .models import *



def signup(request):
    form  = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )
            message.success(request, 'Account was created for '+username)
            return redirect('login')
        ctx = {'form': form}
    return render(request, 'spicyo/signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            pasword = request.POST.get('password')

            user = authenticate(request, username=username, pasword=pasword)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                message.info(request, 'Usename or password is incorrect')
            ctx = {}

    return render(request, 'spicyo/login.html', ctx)


def homepage(request):
    return render(request, 'spicyo/index.html')


def about(request):
    return render(request, 'spicyo/about.html')


def recipe(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes}
    return render(request, 'spicyo/recipe.html', ctx)


def blog(request):
    return render(request, 'spicyo/blog.html')


def contact(request):
    # contact = get_object_or_404(Contact, pk=pk)
    # form = ContactForm()
    # if request.method == 'POST':
    #     form = form(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # ctx = {"form": form}
    return render(request, 'spicyo/contact.html')
