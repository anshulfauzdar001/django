from django.shortcuts import render,redirect
from .models import Recipe
# Create your views here.
def recipe(request):
  if request.method == 'POST':
    data=request.POST
    
    title=data.get('title')
    description=data.get('description')
    ingredients=data.get('ingredients')
    instructions=data.get('instructions')

    Recipe.objects.create(
      title=title,description=description,ingredients=ingredients,
      instructions=instructions)
      
    return redirect('recipe')


  return render(request,'recipe.html')