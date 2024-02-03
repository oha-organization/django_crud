from django.shortcuts import render, get_object_or_404, redirect

from coreapp.models import Person


def home(request):
    return render(request, "fbase1/home.html")


def person_list(request):
    person_list = Person.objects.all()
    return render(request, "fbase1/person_list.html", {"person_list": person_list})


def person_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        person = Person.objects.create(name=name)
        return redirect("fbase1:person-list")
    return render(request, "fbase1/person_create.html")


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, "fbase1/person_detail.html", {"person": person})


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.save()
        return redirect("fbase1:person-detail", pk=person.pk)
    return render(request, "fbase1/person_update.html", {"person": person})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("fbase1:person-list")
    return render(request, "fbase1/person_delete.html", {"name": person.name})
