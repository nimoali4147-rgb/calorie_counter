from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import Form
from django.db.models import Sum

# Create your views here.

def home(request):

    foods = Food.objects.all()

    total_calories = foods.aggregate(   # aggregate - use to calculate total calories
        total=Sum('calories')
    )['total'] or 0

    if request.method == 'POST':

        form = Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = Form()

    return render(request, 'index.html', {
        'foods': foods,
        'total_calories': total_calories,
        'form': form
    })


def delete_food(request, food_id):

    food = get_object_or_404(Food, id=food_id)

    if request.method == 'POST':
        food.delete()

    return redirect('home')


def reset_calories(request):

    if request.method == 'POST':
        Food.objects.all().delete()

    return redirect('home')
