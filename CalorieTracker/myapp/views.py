from django.shortcuts import render, redirect
from .models import Meal
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def meal_list(request):
    search_query = request.GET.get('search', '')
    meals = Meal.objects.filter(user=request.user, name__icontains=search_query).order_by('-date')
    total_calories = sum(meal.calories for meal in meals)

    # Calorie goal and progress percentage
    calorie_goal = 2000  # You can make this dynamic later by storing it in a user profile
    progress_percentage = (total_calories / calorie_goal) * 100 if total_calories <= calorie_goal else 100

    return render(request, 'myapp/meal_list.html', {
        'meals': meals,
        'total_calories': total_calories,
        'progress_percentage': progress_percentage,
    })

@login_required
def add_meal(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = int(request.POST['calories'])
        meal_date = request.POST['date']
        category = request.POST['category']
        Meal.objects.create(user=request.user, name=name, calories=calories, date=meal_date, category=category)
        return redirect('meal_list')
    return render(request, 'myapp/add_meal.html')

@login_required
def daily_summary(request):
    today = date.today()
    meals = Meal.objects.filter(user=request.user, date=today)
    total_calories = sum(meal.calories for meal in meals)
    return render(request, 'myapp/daily_summary.html', {
        'meals': meals,
        'total_calories': total_calories,
    })
