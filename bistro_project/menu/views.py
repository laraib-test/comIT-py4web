from django.shortcuts import render
from .models import Dish 

def menu_view(request): 
# Fetching all items from the "Pantry" 
 all_dishes = Dish.objects.all() 
# # Handing the data to the "Plating Station" 
 return render(request, 'menu.html', {'menu_items': all_dishes})