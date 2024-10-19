from django.urls import path
from . import views

urlpatterns = [
    path("example_get/", views.example_get, name="api_example_get"),
    path("example_post/", views.example_post, name="api_example_post"),

]