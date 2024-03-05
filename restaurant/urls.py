from django.urls import path

from .views import index, DishTypeListView

urlpatterns = [
    path("", index, name='index'),
    path("dishtypes/",
         DishTypeListView.as_view(),
         name="dishtypes-list",)
]

app_name = "restaurant"
