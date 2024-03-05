from django.urls import path

from .views import index, DishTypeListView, CookTypeListView

urlpatterns = [
    path("", index, name='index'),
    path("dishtypes/",
         DishTypeListView.as_view(),
         name="dishtypes-list"),
    path("cooks/", CookTypeListView.as_view(), name="cooks-list"),
]

app_name = "restaurant"
