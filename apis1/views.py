from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from coreapp.models import Person
from .serializers import PersonSerializer, PersonBareMetalSerializer


@api_view(["GET"])
def home(request):
    data = {
        "message": "API 1.0",
        "person_list": request.build_absolute_uri(reverse("apis1:person-list")),
        "person_detail": request.get_full_path() + "{lookup}/",
    }
    return Response(data)


@api_view(["GET", "POST"])
def person_list(request):
    """List all person or create a new one."""
    if request.method == "GET":
        persons = Person.objects.all()
        # serializer = PersonSerializer(persons, many=True)
        serializer = PersonBareMetalSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        # serializer = PersonBareMetalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Person.objects.create(name=serializer.validated_data["name"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def person_detail(request, pk):
    """Retrieve, update or delete a person."""
    try:
        person = get_object_or_404(Person, pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
