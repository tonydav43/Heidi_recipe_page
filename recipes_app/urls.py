from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipes_app'

urlpatterns = [
   path('recipe_search/', views.recipe_search_view, name='recipe_search'),
   path('create/', views.RecipeCreateView.as_view(), name='create'),
   path('list/', views.RecipeListView.as_view(), name='list'),
   path('beef/', views.RecipeBeefListView.as_view(), name='beef'),
   path('pork/', views.RecipePorkListView.as_view(), name='pork'),
   path('lamb/', views.RecipeLambListView.as_view(), name='lamb'),
   path('chicken/', views.RecipeChickenListView.as_view(), name='chicken'),
   path('fish/', views.RecipeFishListView.as_view(), name='fish'),
   path('vegetable/', views.RecipeVegetableListView.as_view(), name='vegetable'),
   path('soup/', views.RecipeSoupListView.as_view(), name='soup'),
   path('dessert/', views.RecipeDessertListView.as_view(), name='dessert'),
   path('cake/', views.RecipeCakeListView.as_view(), name='cake'),
   path('other/', views.RecipeOtherListView.as_view(), name='other'),
   path('detail/<slug:slug>', views.RecipeDetailView.as_view(), name='detail'),
   path('update/<slug:slug>', views.RecipeUpdateView.as_view(), name='update'),
   path('delete/<slug:slug>', views.RecipeDeleteView.as_view(), name='delete'),  
]

