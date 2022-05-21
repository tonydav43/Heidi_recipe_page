from django.contrib import admin
from . models import Recipe

# Register your models here.
# admin.site.register(Recipe)

@admin.register(Recipe)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "recipe_name", "recipe_food_group", "recipe_timestamp", "recipe_updated", "recipe_active")
    search_fields = ("recipe_name",)
    

