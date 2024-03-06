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
)

urlpatterns = [
    path("", index, name='index'),
    path("dishtypes/",
         DishTypeListView.as_view(),
         name="dish_types-list"),
    path("dishtypes/create", DishTypeCreateView.as_view(), name="dish_types-create"),
    path("dishtypes/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish_types-update"),
    path("dishtypes/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish_types-delete"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/create", CookCreateView.as_view(), name="cooks-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dishes-detail"),
    path("dishes/create", DishCreateView.as_view(), name="dish-create")
]

app_name = "restaurant"
