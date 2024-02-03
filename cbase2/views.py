from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from coreapp.models import Person
from .forms import PersonForm


class HomeView(TemplateView):
    template_name = "cbase2/home.html"


class PersonListView(TemplateView):
    template_name = "cbase2/person_list.html"

    def get(self, request, *args, **kwargs):
        person_list = Person.objects.all()
        return render(request, self.template_name, {"person_list": person_list})


class PersonCreateView(TemplateView):
    template_name = "cbase2/person_create.html"
    form_class = PersonForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cbase2:person-detail", pk=form.instance.pk)
        return render(request, self.template_name, {"form": form})


class PersonDetailView(TemplateView):
    template_name = "cbase2/person_detail.html"

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        return render(request, self.template_name, {"person": person})


class PersonUpdateView(TemplateView):
    template_name = "cbase2/person_update.html"
    form_class = PersonForm

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        form = self.form_class(instance=person)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        form = self.form_class(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("cbase2:person-detail", pk=person.pk)
        return render(request, self.template_name, {"form": form})


class PersonDeleteView(TemplateView):
    template_name = "cbase2/person_delete.html"

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        return render(request, self.template_name, {"person": person})

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs["pk"])
        person.delete()
        return redirect("cbase2:person-list")
