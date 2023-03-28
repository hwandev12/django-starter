from django.urls import path
from .views import home, andijon, namangan


urlpatterns = [
    path("", home),
    path("and/", andijon),
    path("nam/", namangan),
]
