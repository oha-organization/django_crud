from django.shortcuts import render
from django.urls import reverse

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from coreapp.models import Person
from .serializers import PersonSerializer


class Home(APIView):
    def get(self, request):
        data = {
            "message": "API 3.0",
            "person_list": request.build_absolute_uri(reverse("apis3:person-list")),
            "person_detail": request.get_full_path() + "{lookup}/",
        }
        return Response(data)


class PersonListApi(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
