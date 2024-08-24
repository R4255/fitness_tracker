from django import forms
from .models import Workout,Diet

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'date', 'duration']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'duration': forms.TimeInput(attrs={'type': 'time', 'step': '1'}),
        }
class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['date', 'calories', 'carbohydrates', 'protein', 'water']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
