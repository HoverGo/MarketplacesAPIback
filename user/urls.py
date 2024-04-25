from django.contrib import admin
from django.urls import path
from .views import RegistrationView


urlpatterns = [
    path("registration/", RegistrationView.as_view()),
]
