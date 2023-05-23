from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-white",
                    "placeholder": "Write a Title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control bg-dark text-white",
                    "placeholder": "Write a description",
                }
            ),
            "important": forms.CheckboxInput(
                attrs={"class": "form-check-input m-auto bg-dark text-white"}
            ),
        }

    def __str__(self):
        pass
