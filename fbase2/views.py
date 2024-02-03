from django.shortcuts import render, get_object_or_404, redirect

from coreapp.models import Person
from .forms import NameForm


def home(request):
    return render(request, "fbase2/home.html")


def person_list(request):
    person_list = Person.objects.all()
    return render(request, "fbase2/person_list.html", {"person_list": person_list})


def person_create(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            Person.objects.create(name=form.cleaned_data["name"])
            return redirect("fbase2:person-list")

    form = NameForm()
    return render(request, "fbase2/person_create.html", {"form": form})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, "fbase2/person_detail.html", {"person": person})


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = NameForm(request.POST, initial={"name": person.name})
        if form.is_valid():
            person.name = form.cleaned_data["name"]
            person.save()
            return redirect("fbase2:person-detail", pk=pk)

    form = NameForm(initial={"name": person.name})
    return render(request, "fbase2/person_update.html", {"form": form})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("fbase2:person-list")
    return render(request, "fbase2/person_delete.html", {"person": person})
