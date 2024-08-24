from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout,Diet
from .forms import WorkoutForm
from django.http import HttpResponse
from datetime import timedelta
from django.utils import timezone

@login_required
def index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'fitness_app/index.html', {'workouts': workouts})

@login_required
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('index')
    return render(request, 'fitness_app/delete_workout.html', {'workout': workout})
@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('index')
    else:
        form = WorkoutForm()
    return render(request, 'fitness_app/add_workout.html', {'form': form})
@login_required
def calculate_bmi(request):
    if request.method == 'GET':
        return render(request, 'fitness_app/calculate_bmi.html')
    elif request.method == 'POST':
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        bmi = weight / (height * height)
        context = {'bmi': f"{bmi:.2f}"}
        return render(request, 'fitness_app/bmi_result.html', context)
# Remove the custom signup view as it's now handled by allauth
@login_required
def calory_track(request):
    user = request.user
    today = timezone.now().date()
    week_start = today - timedelta(days=today.weekday())  # Monday of the current week

    # Weekly intake
    weekly_diet_entries = Diet.objects.filter(user=user, date__gte=week_start)
    weekly_totals = {
        'calories': sum(entry.calories for entry in weekly_diet_entries),
        'carbohydrates': sum(entry.carbohydrates for entry in weekly_diet_entries),
        'protein': sum(entry.protein for entry in weekly_diet_entries),
        'water': sum(entry.water for entry in weekly_diet_entries),
    }

    # All-time intake
    all_time_diet_entries = Diet.objects.filter(user=user)
    all_time_totals = {
        'calories': sum(entry.calories for entry in all_time_diet_entries),
        'carbohydrates': sum(entry.carbohydrates for entry in all_time_diet_entries),
        'protein': sum(entry.protein for entry in all_time_diet_entries),
        'water': sum(entry.water for entry in all_time_diet_entries),
    }

    context = {
        'weekly_totals': weekly_totals,
        'all_time_totals': all_time_totals,
    }

    return render(request, 'fitness_app/calory_track.html', context)