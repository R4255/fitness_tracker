from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout
from .forms import WorkoutForm
from django.http import HttpResponse
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