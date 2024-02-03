from django.shortcuts import render, redirect, get_object_or_404

from coreapp.models import Person
from .forms import PersonForm


def home(request):
    return render(request, "fbase3/home.html")


def person_list(request):
    person_list = Person.objects.all()
    return render(request, "fbase3/person_list.html", {"person_list": person_list})


def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fbase3:person-list")
    form = PersonForm()
    return render(request, "fbase3/person_create.html", {"form": form})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, "fbase3/person_detail.html", {"person": person})


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("fbase3:person-detail", pk=pk)

    form = PersonForm(instance=person)
    return render(request, "fbase3/person_update.html", {"form": form})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("fbase3:person-list")
    return render(request, "fbase3/person_delete.html", {"person": person})
