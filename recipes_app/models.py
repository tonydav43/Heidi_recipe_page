from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Account
from django.utils.text import slugify 
from random import randint
from django.utils import timezone
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

# Create your models here.

def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB, please choose a smaller image" % str(megabyte_limit))

class Recipe(models.Model):
    author = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=155, null=True, unique=True)
    
    catagories = (
        ("Beef", "Beef"),
        ("Pork", "Pork"),
        ("Lamb", "Lamb"),
        ("Chicken", "Chicken"),
        ("Fish", "Fish"),
        ("Vegetable", "Vegetable"),
        ("Soup", "Soup"),
        ("Dessert", "Dessert"),
        ("Cake", "Cake"),
        ("Other", "Other"),
    )
    recipe_name = models.CharField("Recipe Name", max_length=150, help_text="Please enter a recipe name")
    recipe_country = CountryField("Country", help_text="Please select a country", default= "No country selected")
    recipe_food_group = models.CharField("Recipe Food Group", max_length=50, choices=catagories, help_text="Please select the food group from the dropdown menu") 
    recipe_ingredients = models.TextField("Recipe Ingredients", max_length=5000, help_text="Please enter the ingredients and quantities to be used")
    recipe_instructions = models.TextField("Recipe Instructions", max_length=25000, help_text="Please enter the instructions for the recipe")
    recipe_notes = models.TextField("Recipe Notes", max_length=5000, help_text="Please enter any notes for the recipe", blank=True, default="There are currently no notes associated with this recipe")
    recipe_image = models.ImageField("Recipe Image", help_text="Please upload an image, a default image will be used if none selected", upload_to='images', blank=True, default='images/default.png', validators=[validate_image])
    recipe_timestamp = models.DateField(auto_now_add=True)
    recipe_updated = models.DateTimeField(auto_now=True)
    recipe_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):

        if self.slug:
            if self.slug == self.slug:
               self.slug = self.slug
        elif Recipe.objects.filter(recipe_name=self.recipe_name).exists():
             extra = str(randint(1, 10000))
             self.slug = slugify(self.recipe_name) + "-" + extra    
        else:
            self.slug = slugify(self.recipe_name)
        return super(Recipe, self).save(*args, **kwargs) 
    
    def __str__(self):
        return f"The author of this recipe is {self.author}"


