from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Dish, Cook


class PublicDishTypesTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(reverse("restaurant:dish_types-list"))
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self) -> None:
        DishType.objects.create(name="test1")
        response = self.client.get(reverse("restaurant:dish_types-list"))
        self.assertEqual(response.status_code, 200)


class PublicDishTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(reverse("restaurant:dishes-list"))
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dishes(self) -> None:
        dish_type = DishType.objects.create(name="test1")
        Dish.objects.create(name="test2", price=43, description="test3", dish_type=dish_type)
        response = self.client.get(reverse("restaurant:dishes-list"))
        self.assertEqual(response.status_code, 200)


class PublicCookTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(reverse("restaurant:cooks-list"))
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self) -> None:
        response = self.client.get(reverse("restaurant:cooks-list"))
        self.assertEqual(response.status_code, 200)


class DishListViewSearchTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password"
        )
        self.client.login(username="testuser", password="password")
        pizza_type = DishType.objects.create(name="pizza")
        sushi_type = DishType.objects.create(name="sushi")
        sup_type = DishType.objects.create(name="sup")

        Dish.objects.create(
            name="test1",
            description="test_description1",
            price=11,
            dish_type=pizza_type
        )
        Dish.objects.create(
            name="test2",
            price=33,
            description="test_description2",
            dish_type=sushi_type
        )
        Dish.objects.create(
            name="test3",
            price=333,
            description="test_description3",
            dish_type=sup_type
        )

    def test_dish_list_view_with_search(self) -> None:
        url = reverse("restaurant:dishes-list")
        response = self.client.get(url, {"name": "test1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test1")
        self.assertNotContains(response, "test2")
        self.assertNotContains(response, "tes3")


class DishTypeListViewSearchTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password"
        )
        self.client.login(username="test", password="password")
        DishType.objects.create(name="pizza")
        DishType.objects.create(name="sushi")
        DishType.objects.create(name="sup")

    def test_dish_types_list_view_with_search(self) -> None:
        url = reverse("restaurant:dish_types-list")
        response = self.client.get(url, {"name": "pizza"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pizza")
        self.assertNotContains(response, "sushi")
        self.assertNotContains(response, "sup")


class CookListViewSearchTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password"
        )
        self.client.login(username="test", password="password")
        Cook.objects.create(username="Bob", password="test1")
        Cook.objects.create(username="Alice", password="test2")

    def test_cook_list_view_with_search(self) -> None:
        url = reverse("restaurant:cooks-list")
        response = self.client.get(url, {"username": "Bob"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bob")
        self.assertNotContains(response, "Alice")
