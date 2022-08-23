from .models import Recipe
from django import forms
from django_countries.widgets import CountrySelectWidget
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('recipe_active', 'author', 'slug')
        labels = {
            'recipe_name': _("Recipe Name"),
            'recipe_country': _("Recipe Country"),
            'recipe_food_group': _("Recipe Food Group"),
            'recipe_ingredients': _("Recipe Ingredients"),
            'recipe_instructions': _("Recipe Instructions"),
            'recipe_notes': _("Recipe Notes"), 
            'recipe_image': _("Recipe Image"),
        }

        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_country': CountrySelectWidget(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_food_group': forms.Select(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_ingredients': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_instructions': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_notes': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_image': forms.FileInput(attrs={'class': "form-label", 'class': "form-control"}),
        }

class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('recipe_active', 'author', 'slug')

        labels = {
            'recipe_name': _("Recipe Name"),
            'recipe_country': _("Recipe Country"),
            'recipe_food_group': _("Recipe Food Group"),
            'recipe_ingredients': _("Recipe Ingredients"),
            'recipe_instructions': _("Recipe Instructions"),
            'recipe_notes': _("Recipe Notes"),
            'recipe_image': _("Recipe Image"), 
        }
        
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_country': CountrySelectWidget(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_food_group': forms.Select(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_ingredients': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_instructions': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_notes': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_image': forms.FileInput(attrs={'class': "form-label", 'class': "form-control"}), # if you remove this the checkbox comes back
        }

        help_texts = {
            'recipe_name': _("Update the recipe name here."),
            'recipe_country': _("Update the country here."),
            'recipe_food_group': _("Update the recipe food group here."),
            'recipe_ingredients': _("Update the recipe ingredients here."),
            'recipe_instructions': _("Update the ingredient instructions here."),
            'recipe_notes': _("Update the recipe notes here."),
            'recipe_image': _("Update the recipe image here."),
        }
 
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['recipe_image'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        #     self.fields['recipe_image'].widget.recipe_image_clear_id = "Help"
        #     self.fields['recipe_image'].widget.input_text = _("Choose a file to change the current image") 

