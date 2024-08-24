from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    duration = models.DurationField()
    def __str__(self):
        return self.name
class Diet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.IntegerField(default=0)
    carbohydrates = models.IntegerField(default=0)  # in grams
    protein = models.IntegerField(default=0)        # in grams
    water = models.IntegerField(default=0)          # in milliliters

    def __str__(self):
        return f"{self.user.username} - {self.date}"
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    target_date = models.DateField()

    def __str__(self):
        return self.description
  