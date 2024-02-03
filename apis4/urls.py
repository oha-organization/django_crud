from django.urls import path

from . import views


app_name = "apis4"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("persons/", views.PersonListApi.as_view(), name="person-list"),
    path("persons/<int:pk>/", views.PersonDetailApi.as_view(), name="person-detail"),
]
