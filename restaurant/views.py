from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.forms import CookCreationForm, CookUpdateForm, DishTypeSearchForm, CookSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return (queryset.filter
                    (name__icontains=form.cleaned_data["name"])
                    )
        return queryset


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return (queryset.filter
                    (username__icontains=form.cleaned_data["username"])
                    )
        return queryset


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("restaurant:cooks-list")


class CookUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("restaurant:cooks-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
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


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dishes-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dishes-list")
