from django.urls import path
from . import views

urlpatterns = [
    path('', views.applehome, name="homepage"),
]
