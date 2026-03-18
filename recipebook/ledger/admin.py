from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage

# Register your models here.

class RecipeInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInLine,]
    search_fields = ('name',)

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

    fieldsets = [
        ("Details", 
         {'fields':[
             'recipe_image',
             'description', 
             'recipe'
             ]
                     })
    ]

admin.site.register(Recipe,RecipeAdmin)
admin.site.register(RecipeImage,RecipeImageAdmin)