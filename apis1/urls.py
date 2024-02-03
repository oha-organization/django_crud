from django.urls import path

from . import views


app_name = "apis1"
urlpatterns = [
    path("", views.home, name="home"),
    path("persons/", views.person_list, name="person-list"),
    path("persons/<int:pk>/", views.person_detail, name="person-detail"),
]
