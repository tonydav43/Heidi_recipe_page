# Generated by Django 4.0.4 on 2022-05-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0008_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=155, null=True, unique=True),
        ),
    ]
