from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from restaurant.models import DishType, Dish, Cook


def index(request):
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
    }

    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(ListView):
    model = DishType
    context_object_name = "dish_types_list"
    template_name = "restaurant/dish_types_list.html"
    paginate_by = 5


class CookListView(ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "restaurant/cook_list.html"
    paginate_by = 5


class CookDetailView(DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class DishListView(ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "restaurant/dish_list.html"
    paginate_by = 5


class DishDetailView(DetailView):
    model = Dish

