from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'

class RecipeDetailView(LoginRequiredMixin,DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_create.html'
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipes_list')

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'recipe_create_image.html'
    form_class = RecipeImageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(pk = self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', 
                            kwargs={'pk': self.object.recipe.pk })
    
def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes,
    }

    return render(request, 'recipes_list.html', ctx)

def recipe_add_image(request):
    form = RecipeImageForm()

    ctx = {
        "form": form
    }

    if request.method== 'POST':
        form = RecipeImageForm(request.POST)
        if form.is_valid():
            image = form.save()
    return render(request, 'recipe_create_image.html', ctx)

# Create your views here.