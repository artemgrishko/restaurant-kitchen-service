from django.test import TestCase

from restaurant.forms import CookCreationForm


class TestForms(TestCase):
    def test_cook_creation_form_is_valid(self) -> None:
        form_data = {
            "username": "test_username",
            "password1": "test_password",
            "password2": "test_password",
            "years_of_experience": 7,
            "first_name": "test_first_name",
            "last_name": "test_last_name",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
