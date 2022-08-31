from django.urls import path
from api.views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', login, name='login'),
    path('homepage/', homepage, name="homepage"),
    path('about/', about, name="about"),
    path('recipe/', recipe, name="recipe"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
]
