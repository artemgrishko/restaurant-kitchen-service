from django.urls import path

from .views import index, DishTypeListView, CookListView, DishListView, CookDetailView

urlpatterns = [
    path("", index, name='index'),
    path("dishtypes/",
         DishTypeListView.as_view(),
         name="dish_types-list"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("dishes/", DishListView.as_view(), name="dishes-list")
]

app_name = "restaurant"
