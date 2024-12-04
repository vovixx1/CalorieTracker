from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    objects = models.Manager()  # This is not needed, it’s automatically provided by Django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    meal_type = models.CharField(
        max_length=50,
        choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')],
    )
    calories = models.IntegerField()
    date = models.DateTimeField()  # Updated to include time

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"
