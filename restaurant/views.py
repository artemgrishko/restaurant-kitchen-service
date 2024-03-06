from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.forms import CookCreationForm
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


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_types_list"
    template_name = "restaurant/dish_types_list.html"
    paginate_by = 5


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish_form.html"
    success_url = reverse_lazy("restaurant:dish_types-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish_types-list")
    template_name = "restaurant/dish_types_form.html"


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dish_types-list")
    template_name = "restaurant/dish_types_confirm_delete.html"


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "restaurant/cook_list.html"
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("restaurant:cooks-list")


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "restaurant/dish_list.html"
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dishes-list")
