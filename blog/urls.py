from django.urls import path
from .views import *


urlpatterns = [
    path("", home),
    path("and/", andijon),
    path("nam/", namangan),
    path("buxoro/", buxoro),
    path("books/", books)
]
