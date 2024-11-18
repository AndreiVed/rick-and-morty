from tkinter.font import names

from django.urls import path
from rest_framework.urls import app_name

from characters.views import get_random_character_view


app_name = "characters"
urlpatterns = [
    path("characters/random", get_random_character_view, name="character_random"),
]
