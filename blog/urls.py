from django.urls import path
from .views import home, andijon, namangan, buxoro


urlpatterns = [
    path("", home),
    path("and/", andijon),
    path("nam/", namangan),
    path("buxoro/", buxoro)
]
