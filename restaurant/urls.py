from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishListView,
    CookDetailView,
    DishDetailView,
    CookListView,
    DishCreateView,
    DishTypeCreateView,
    CookCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookUpdateView,
    CookDeleteView,
    DishUpdateView,
    DishDeleteView,
)

urlpatterns = [
    path("", index, name='index'),
    path("dishtypes/",
         DishTypeListView.as_view(),
         name="dish_types-list"),
    path("dishtypes/create/", DishTypeCreateView.as_view(), name="dish_types-create"),
    path("dishtypes/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish_types-update"),
    path("dishtypes/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish_types-delete"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cooks-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cooks-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cooks-delete"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dishes-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
]

app_name = "restaurant"
