from django.urls import path

from . import views


app_name = "coreapp"
urlpatterns = [
    path("", views.home, name="home"),
]
