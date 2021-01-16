from django.urls import path
from . import views

urlpatterns = [
    path("pp/", views.index, name="index"),
]