from django import forms
from django.contrib.auth.forms import UserCreationForm

from restaurant.models import Cook


class CookCreationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience", "first_name", "last_name",)
