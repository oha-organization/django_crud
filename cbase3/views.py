from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from coreapp.models import Person


class HomeView(TemplateView):
    template_name = "cbase3/home.html"


class PersonListView(ListView):
    model = Person
    template_name = "cbase3/person_list.html"
    context_object_name = "person_list"


class PersonDetailView(DetailView):
    model = Person
    template_name = "cbase3/person_detail.html"


class PersonCreateView(CreateView):
    model = Person
    template_name = "cbase3/person_create.html"
    fields = ["name"]
    success_url = reverse_lazy("cbase3:person-list")


class PersonUpdateView(UpdateView):
    model = Person
    template_name = "cbase3/person_update.html"
    fields = ["name"]
    success_url = reverse_lazy("cbase3:person-list")


class PersonDeleteView(DeleteView):
    model = Person
    template_name = "cbase3/person_delete.html"
    success_url = reverse_lazy("cbase3:person-list")
