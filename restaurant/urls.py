from django.urls import path

from .views import index, DishTypeListView, CookListView, DishListView

urlpatterns = [
    path("", index, name='index'),
    path("dishtypes/",
         DishTypeListView.as_view(),
         name="dishtypes-list"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("dishes/", DishListView.as_view(), name="dishes-list")
]

app_name = "restaurant"
