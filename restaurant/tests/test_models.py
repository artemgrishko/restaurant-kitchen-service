from django.test import TestCase

from restaurant.models import DishType, Cook


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")

        self.assertEqual(str(dish_type), "test")

    def test_cook_with_years_of_exercise(self):
        username = "test_username"
        password = "test_password"
        years_of_experience = 6
        cook = Cook.objects.create(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertEqual(cook.password, password)
        self.assertEqual(cook.years_of_experience, years_of_experience)
