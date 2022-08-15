from django.shortcuts import render
from .forms import RecipeForm, RecipeUpdateForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Recipe
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q 

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('recipes_app:list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(CreateView, self).form_valid(form)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_app/recipe_list.html'
    queryset = Recipe.objects.order_by('-recipe_timestamp') 
    context_object_name = 'recipe_list'
    paginate_by = 12
    
class RecipeBeefListView(ListView):
    model = Recipe
    template_name = 'recipes_app/beef_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Beef") | Q(recipe_food_group__icontains="Storfekjøtt")).order_by('-recipe_timestamp')
    context_object_name = 'beef_recipe_list' 
    paginate_by = 12

class RecipePorkListView(ListView):
    model = Recipe
    template_name = 'recipes_app/pork_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Pork") | Q(recipe_food_group__icontains="Svenekjøtt")).order_by('-recipe_timestamp')
    context_object_name = 'pork_recipe_list' 
    paginate_by = 12

class RecipeLambListView(ListView):
    model = Recipe
    template_name = 'recipes_app/lamb_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Lamb") | Q(recipe_food_group__icontains="Lam")).order_by('-recipe_timestamp') 
    context_object_name = 'lamb_recipe_list' 
    paginate_by = 12

class RecipeChickenListView(ListView):
    model = Recipe
    template_name = 'recipes_app/chicken_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Chicken") | Q(recipe_food_group__icontains="Kylling")).order_by('-recipe_timestamp') 
    context_object_name = 'chicken_recipe_list' 
    paginate_by = 12

class RecipeFishListView(ListView):
    model = Recipe
    template_name = 'recipes_app/fish_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Fish") | Q(recipe_food_group__icontains="Fisk")).order_by('-recipe_timestamp')
    context_object_name = 'fish_recipe_list' 
    paginate_by = 12

class RecipeVegetableListView(ListView):
    model = Recipe
    template_name = 'recipes_app/vegetable_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Vegetables") | Q(recipe_food_group__icontains="Grønsaker")).order_by('-recipe_timestamp') 
    context_object_name = 'vegetable_recipe_list' 
    paginate_by = 12    

class RecipeSoupListView(ListView):
    model = Recipe
    template_name = 'recipes_app/soup_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Soups") | Q(recipe_food_group__icontains="Supper")).order_by('-recipe_timestamp') 
    context_object_name = 'soup_recipe_list' 
    paginate_by = 12

class RecipeDessertListView(ListView):
    model = Recipe
    template_name = 'recipes_app/dessert_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Desserts") | Q(recipe_food_group__icontains="Desserter")).order_by('-recipe_timestamp') 
    context_object_name = 'dessert_recipe_list' 
    paginate_by = 12

class RecipeCakeListView(ListView):
    model = Recipe
    template_name = 'recipes_app/cake_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Cakes") | Q(recipe_food_group__icontains="Kaker")).order_by('-recipe_timestamp') 
    context_object_name = 'cake_recipe_list' 
    paginate_by = 12

class RecipeOtherListView(ListView):
    model = Recipe
    template_name = 'recipes_app/other_list.html'
    queryset = Recipe.objects.filter(Q(recipe_food_group__icontains="Others") | Q(recipe_food_group__icontains="Andre")).order_by('-recipe_timestamp')
    context_object_name = 'other_recipe_list' 
    paginate_by = 12

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes_app/recipe_detail.html'
    
class RecipeUpdateView(UpdateView):
    model = Recipe 
    form_class = RecipeUpdateForm
    template_name = 'recipes_app/recipe_update.html'
    
    def get_success_url(self):
        return reverse_lazy('recipes_app:detail', kwargs={'slug': self.kwargs['slug']})

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes_app/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes_app:list')

def recipe_search_view(request):
    if request.method == "POST":
        searched = request.POST['searched']
        lookups = Q(recipe_name__icontains=(searched)) | Q(recipe_ingredients__icontains=(searched))
        recipes = Recipe.objects.filter(lookups)
        paginator = Paginator(recipes, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "recipes_app/recipe_search.html", {'searched': searched, 'recipes': recipes, 'page_obj':page_obj})
    else:
        return render(request, "recipes_app/recipe_search.html", {})

def language_view(request):
    return render(request, 'recipes_app/language.html')
    


