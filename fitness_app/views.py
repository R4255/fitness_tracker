from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout,Diet
from .forms import WorkoutForm,DietForm
from django.http import HttpResponse
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)


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
    try:
        user = request.user
        today = timezone.localtime().date()
        week_start = today - timedelta(days=today.weekday())

        weekly_diet_entries = Diet.objects.filter(user=user, date__gte=week_start)
        logger.info(f"Weekly entries count: {weekly_diet_entries.count()}")

        weekly_totals = {
            'calories': sum(entry.calories or 0 for entry in weekly_diet_entries),
            'carbohydrates': sum(entry.carbohydrates or 0 for entry in weekly_diet_entries),
            'protein': sum(entry.protein or 0 for entry in weekly_diet_entries),
            'water': sum(entry.water or 0 for entry in weekly_diet_entries),
        }
        logger.info(f"Weekly totals: {weekly_totals}")

        all_time_diet_entries = Diet.objects.filter(user=user)
        logger.info(f"All-time entries count: {all_time_diet_entries.count()}")

        all_time_totals = {
            'calories': sum(entry.calories or 0 for entry in all_time_diet_entries),
            'carbohydrates': sum(entry.carbohydrates or 0 for entry in all_time_diet_entries),
            'protein': sum(entry.protein or 0 for entry in all_time_diet_entries),
            'water': sum(entry.water or 0 for entry in all_time_diet_entries),
        }
        logger.info(f"All-time totals: {all_time_totals}")

        context = {
            'weekly_totals': weekly_totals,
            'all_time_totals': all_time_totals,
        }

        return render(request, 'fitness_app/calory_track.html', context)
    except Exception as e:
        logger.error(f"Error in calory_track view: {str(e)}", exc_info=True)
        return HttpResponse("An error occurred. Please try again later.", status=500)
@login_required
def add_diet_entry(request):
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            try:
                diet_entry = form.save(commit=False)
                diet_entry.user = request.user
                diet_entry.save()
                return redirect('calory_track')
            except Exception as e:
                logger.error(f"Error saving diet entry: {str(e)}")
                messages.error(request, "An error occurred while saving your diet entry. Please try again.")
        else:
            logger.error(f"Form validation errors: {form.errors}")
    else:
        form = DietForm()
    return render(request, 'fitness_app/add_diet_entry.html', {'form': form})