from django.urls import path

from . import views


app_name = "cbase1"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("persons/", views.PersonListView.as_view(), name="person-list"),
    path("persons/create/", views.PersonCreateView.as_view(), name="person-create"),
    path("persons/<int:pk>/", views.PersonDetailView.as_view(), name="person-detail"),
    path(
        "persons/<int:pk>/update/",
        views.PersonUpdateView.as_view(),
        name="person-update",
    ),
    path(
        "persons/<int:pk>/delete/",
        views.PersonDeleteView.as_view(),
        name="person-delete",
    ),
]
