from django.http import Http404
from django.urls import reverse

from rest_framework import status
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from coreapp.models import Person


class Home(APIView):
    def get(self, request):
        data = {
            "message": "API 4.0",
            "person_list": request.build_absolute_uri(reverse("apis4:person-list")),
            "person_detail": request.get_full_path() + "{lookup}/",
        }
        return Response(data)


class PersonListApi(APIView):
    """List all persons, or create new person."""

    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = ["id", "name"]

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = ["id", "name"]

    def get(self, request):
        persons = Person.objects.all()
        serializer = self.OutputSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        if serializer.is_valid():
            # Easy way to use Object level permission
            if request.user.is_superuser:
                serializer.validated_data["name"] += " Logged By Super User"
            else:
                serializer.validated_data["name"] += f" Logged By {request.user}"
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailApi(APIView):
    """
    Retrieve, update or delete a person instance.
    """

    permission_classes = [permissions.IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = ["id", "name"]

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = ["name"]

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = self.OutputSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = self.InputSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if request.user.is_superuser:
            snippet = self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "FAILED! Only admin can delete."},
            status=status.HTTP_403_FORBIDDEN,
        )
