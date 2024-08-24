# In your forms.py
from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'date', 'duration']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Use a time input for duration
        }
    duration=forms.DurationField(
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 1:30:00 for 1 hour 30 minutes'})
    )