from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    duration = models.DurationField()
    def __str__(self):
        return self.name
class Diet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    target_date = models.DateField()

    def __str__(self):
        return self.description
  