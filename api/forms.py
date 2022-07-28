from django.forms import ModelForm
from django import forms
from .models import *


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
