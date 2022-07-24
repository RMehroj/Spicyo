from django.urls import path
from api.views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('about/', about, name="about"),
    path('recipe/', recipe, name="recipe"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
]
