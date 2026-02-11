"""
URL configuration for recipebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import recipes_list, recipe_1, recipe_2

urlpatterns = [
    path('recipes/list', recipes_list,name="recipes_list"),
    path('recipe/1', recipe_1, name="recipe_1"),
    path('recipe/2', recipe_2, name="recipe_2"),
]

app_name='ledger'