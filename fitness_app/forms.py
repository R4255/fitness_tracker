# In your forms.py
from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'date', 'duration']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'duration': forms.TimeInput(attrs={'type': 'time'}),  # Use a time input for duration
        }