from django.urls import path

from . import views


app_name = "fbase2"
urlpatterns = [
    path("", views.home, name="home"),
    path("persons/", views.person_list, name="person-list"),
    path("persons/create/", views.person_create, name="person-create"),
    path("persons/<int:pk>/", views.person_detail, name="person-detail"),
    path("persons/<int:pk>/update/", views.person_update, name="person-update"),
    path("persons/<int:pk>/delete/", views.person_delete, name="person-delete"),
]
