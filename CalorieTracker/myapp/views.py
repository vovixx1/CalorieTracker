from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Sum
from accounts.models import UserProfile
from .forms import MealForm




@login_required
def meal_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    total_calories = meals.aggregate(total=Sum('calories'))['total'] or 0
    calorie_goal = user_profile.calorie_goal or 2000

    # Precompute the percentage and progress class
    percentage_consumed = (total_calories / calorie_goal) * 100 if calorie_goal > 0 else 0
    progress_class = 'bg-success' if total_calories <= calorie_goal else 'bg-danger'

    if request.method == "POST":
        calorie_goal = request.POST.get('calorie_goal')
        if calorie_goal.isdigit():
            user_profile.calorie_goal = int(calorie_goal)
            user_profile.save()
            return redirect('meal_list')

    context = {
        'meals': meals,
        'total_calories': total_calories,
        'calorie_goal': calorie_goal,
        'percentage_consumed': percentage_consumed,
        'progress_class': progress_class,
    }
    return render(request, 'myapp/meal_list.html', context)


@login_required
def add_meal(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('meal_list')
    else:
        form = MealForm()

    return render(request, 'myapp/add_meal.html', {'form': form})

@login_required
def daily_summary(request):
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    total_calories = meals.aggregate(total=Sum('calories'))['total'] or 0
    calorie_goal = 2000  # Or fetch from the UserProfile if you've set it
    percentage_consumed = (total_calories / calorie_goal) * 100 if calorie_goal > 0 else 0

    context = {
        'meals': meals,
        'total_calories': total_calories,
        'calorie_goal': calorie_goal,
        'percentage_consumed': percentage_consumed,
    }
    return render(request, 'myapp/daily_summary.html', context)

def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, user=request.user)
    if request.method == "POST":
        meal.delete()
        return redirect('meal_list')  # Redirect to the list of meals after deletion
    return render(request, 'myapp/confirm_delete.html', {'meal': meal})