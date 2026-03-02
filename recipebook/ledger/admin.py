from django.contrib import admin
from .models import Recipe, RecipeIngredient

# Register your models here.

class RecipeInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInLine,]
    search_fields = ('name',)

admin.site.register(Recipe,RecipeAdmin)