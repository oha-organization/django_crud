from django import forms

from coreapp.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name"]
