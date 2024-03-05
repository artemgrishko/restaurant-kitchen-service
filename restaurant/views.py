from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

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
    context_object_name = "dishtypes_list"
    template_name = "restaurant/dishtypes_list.html"
    paginate_by = 5