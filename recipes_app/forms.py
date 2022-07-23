from .models import Recipe
from django import forms
from django_countries.widgets import CountrySelectWidget

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('recipe_active', 'author', 'slug')
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_country': CountrySelectWidget(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_food_group': forms.Select(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_ingredients': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_instructions': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_notes': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipe_image'].widget.attrs.update({'class': "form-label", 'class': "form-control"})

class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('recipe_active', 'author', 'slug')
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_country': CountrySelectWidget(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_food_group': forms.Select(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_ingredients': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_instructions': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
            'recipe_notes': forms.Textarea(attrs={'class': "form-label", 'class': "form-control"}),
        }
        help_texts = {
            'recipe_name': ('Update the recipe name here.'),
            'recipe_country': ('Update the country here.'),
            'recipe_food_group': ('Update the recipe food group here.'),
            'recipe_ingredients': ('Update the recipe ingredients here.'),
            'recipe_instructions': ('Update the ingredient instructions here.'),
            'recipe_notes': ('Update the recipe notes here.'),
            'recipe_image': ('Update the recipe image here.'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipe_image'].widget.attrs.update({'class': "form-label", 'class': "form-control"})

        

       
        
