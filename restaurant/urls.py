from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishListView,
    CookDetailView,
    DishDetailView,
)

urlpatterns = [
    path("", index, name='index'),
    path("dishtypes/",
         DishTypeListView.as_view(),
         name="dish_types-list"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dishes-detail"),
]

app_name = "restaurant"
