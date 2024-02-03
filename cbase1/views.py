from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import View

from coreapp.models import Person
from .forms import NameForm


class HomeView(TemplateView):
    template_name = "cbase1/home.html"


class PersonListView(View):
    def get(self, request, *args, **kwargs):
        person_list = Person.objects.all()
        return render(request, "cbase1/person_list.html", {"person_list": person_list})


class PersonCreateView(View):
    form_class = NameForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, "cbase1/person_create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            person = Person.objects.create(name=form.cleaned_data["name"])
            return redirect("cbase1:person-detail", pk=person.pk)

        return render(request, "cbase1/person_create.html", {"form": form})


class PersonDetailView(View):
    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        return render(request, "cbase1/person_detail.html", {"person": person})


class PersonUpdateView(View):
    form_class = NameForm

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        form = self.form_class(initial={"name": person.name})
        return render(request, "cbase1/person_update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        form = self.form_class(request.POST)
        if form.is_valid():
            person.name = form.cleaned_data["name"]
            person.save()
            return redirect("cbase1:person-detail", pk=kwargs["pk"])
        return render(request, "cbase1/person_update.html", {"form": form})


class PersonDeleteView(View):
    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        return render(request, "cbase1/person_delete.html", {"person": person})

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        person.delete()
        return redirect("cbase1:person-list")
